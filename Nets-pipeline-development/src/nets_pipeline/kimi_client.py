"""Kimi / Moonshot API wrapper.

Per §11 "Kimi API Configuration":
  - Model: kimi-k2-0711-preview via api.moonshot.ai/v1
  - OpenAI-compatible SDK works with base URL swapped
  - response_format: json_object (structured output mode)
  - temperature: 0.3, max_tokens: 8000
  - Cache discipline: system message = cacheable prefix (Layers 1-5),
    user message = dynamic (Layers 6-8)
  - Retry: transient errors → exponential backoff, max 5 attempts

Returns both the parsed JSON output and usage metadata so the caller
can log cache-hit %, tokens, latency, cost (§13).
"""
from __future__ import annotations

import asyncio
import json
import time
from dataclasses import dataclass
from typing import Any

from openai import APIConnectionError, APIError, AsyncOpenAI, RateLimitError

from .config import Settings

# Pricing per §11, in USD per million tokens
PRICE_IN_PER_M = 0.60
PRICE_OUT_PER_M = 2.50
PRICE_CACHED_PER_M = 0.15


@dataclass
class CallResult:
    output_json: dict[str, Any]
    raw_content: str
    tokens_in: int
    tokens_out: int
    tokens_cached: int
    cache_hit_pct: float
    cost_usd: float
    latency_ms: int


class KimiClient:
    def __init__(self, settings: Settings) -> None:
        if not settings.moonshot_api_key:
            raise RuntimeError(
                "MOONSHOT_API_KEY is not set. Required for any command that "
                "calls Kimi (run). Add it to .env — see .env.example."
            )
        self.settings = settings
        self._client = AsyncOpenAI(
            api_key=settings.moonshot_api_key,
            base_url=settings.moonshot_base_url,
        )

    async def call(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 8000,
        temperature: float = 0.3,
        max_attempts: int = 5,
    ) -> CallResult:
        """Issue one Kimi call. Retries transient errors with exponential backoff."""
        start = time.monotonic()
        last_err: Exception | None = None

        for attempt in range(1, max_attempts + 1):
            try:
                resp = await self._client.chat.completions.create(
                    model=self.settings.moonshot_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    response_format={"type": "json_object"},
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                latency_ms = int((time.monotonic() - start) * 1000)
                return self._parse_response(resp, latency_ms)

            except (RateLimitError, APIConnectionError) as e:
                last_err = e
                backoff = min(2 ** attempt, 32)
                await asyncio.sleep(backoff)
            except APIError as e:
                # 5xx → retry; 4xx (other than 429) → fail fast
                if 500 <= getattr(e, "status_code", 0) < 600:
                    last_err = e
                    backoff = min(2 ** attempt, 32)
                    await asyncio.sleep(backoff)
                else:
                    raise

        raise RuntimeError(
            f"Kimi call failed after {max_attempts} attempts: {last_err}"
        ) from last_err

    def _parse_response(self, resp: Any, latency_ms: int) -> CallResult:
        content = resp.choices[0].message.content or ""
        try:
            output = json.loads(content)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Kimi returned malformed JSON: {e}") from e

        usage = getattr(resp, "usage", None)
        tokens_in = getattr(usage, "prompt_tokens", 0) if usage else 0
        tokens_out = getattr(usage, "completion_tokens", 0) if usage else 0

        # Cached tokens reported by Moonshot in usage.prompt_tokens_details.cached_tokens
        # (OpenAI-compatible; field may be under different names).
        cached = 0
        if usage is not None:
            details = getattr(usage, "prompt_tokens_details", None)
            if details is not None:
                cached = getattr(details, "cached_tokens", 0) or 0

        cache_hit_pct = (cached / tokens_in * 100.0) if tokens_in else 0.0

        uncached_in = max(tokens_in - cached, 0)
        cost = (
            uncached_in * PRICE_IN_PER_M / 1_000_000
            + cached * PRICE_CACHED_PER_M / 1_000_000
            + tokens_out * PRICE_OUT_PER_M / 1_000_000
        )

        return CallResult(
            output_json=output,
            raw_content=content,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            tokens_cached=cached,
            cache_hit_pct=cache_hit_pct,
            cost_usd=cost,
            latency_ms=latency_ms,
        )
