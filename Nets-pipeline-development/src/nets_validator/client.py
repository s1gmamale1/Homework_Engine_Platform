"""Validator model client.

§14 specifies a cheaper cross-family model — Haiku 4.5 (Anthropic) or
Gemini Flash (Google) — to avoid in-family blind spots.

Provider selected via VALIDATOR_PROVIDER env var. Supported:
  - anthropic  (default)
  - google

Gemini path is deferred — anthropic is the initial implementation path
since §14 lists Haiku 4.5 first and its SDK is familiar.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass

from nets_pipeline.config import Settings


@dataclass
class ValidatorCallResult:
    output_json: dict
    raw_content: str
    tokens_in: int
    tokens_out: int
    latency_ms: int


class ValidatorClient:
    def __init__(self, settings: Settings) -> None:
        provider = (settings.validator_provider or "anthropic").lower()
        if provider == "anthropic":
            self._impl: _AnthropicValidator | _GeminiValidator = _AnthropicValidator(
                settings
            )
        elif provider == "google":
            self._impl = _GeminiValidator(settings)
        else:
            raise ValueError(
                f"Unknown VALIDATOR_PROVIDER: {provider!r}. "
                "Use 'anthropic' or 'google'."
            )

    @property
    def model_name(self) -> str:
        return self._impl.model_name

    async def call(self, *, system_prompt: str, user_prompt: str) -> ValidatorCallResult:
        return await self._impl.call(
            system_prompt=system_prompt, user_prompt=user_prompt
        )


class _AnthropicValidator:
    def __init__(self, settings: Settings) -> None:
        try:
            from anthropic import AsyncAnthropic
        except ImportError as e:
            raise ImportError(
                "anthropic package required for Anthropic validator. "
                "Install with: pip install -e '.[validator]'"
            ) from e

        if not settings.anthropic_api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY is required when VALIDATOR_PROVIDER=anthropic"
            )

        self.model_name = settings.validator_model or "claude-haiku-4-5-20251001"
        self._client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    async def call(self, *, system_prompt: str, user_prompt: str) -> ValidatorCallResult:
        start = time.monotonic()
        resp = await self._client.messages.create(
            model=self.model_name,
            max_tokens=2000,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        latency_ms = int((time.monotonic() - start) * 1000)

        text_parts = [b.text for b in resp.content if getattr(b, "type", "") == "text"]
        raw = "".join(text_parts).strip()

        # Strip optional ```json fences if the model emitted them anyway
        if raw.startswith("```"):
            raw = raw.strip("`")
            if raw.lower().startswith("json"):
                raw = raw[4:]
            raw = raw.strip()

        try:
            output = json.loads(raw)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Validator returned malformed JSON: {e}") from e

        usage = getattr(resp, "usage", None)
        tokens_in = getattr(usage, "input_tokens", 0) if usage else 0
        tokens_out = getattr(usage, "output_tokens", 0) if usage else 0

        return ValidatorCallResult(
            output_json=output,
            raw_content=raw,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            latency_ms=latency_ms,
        )


class _GeminiValidator:
    def __init__(self, settings: Settings) -> None:
        self.model_name = settings.validator_model or "gemini-2.5-flash"
        self._settings = settings
        raise NotImplementedError(
            "Gemini validator not yet implemented. Set VALIDATOR_PROVIDER=anthropic "
            "or implement this class when ready."
        )

    async def call(self, *, system_prompt: str, user_prompt: str) -> ValidatorCallResult:
        raise NotImplementedError
