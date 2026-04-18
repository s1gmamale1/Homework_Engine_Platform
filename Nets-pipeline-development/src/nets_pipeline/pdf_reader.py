"""PDF → text extraction.

Tries pdfplumber first (clean text layout). Falls back to pymupdf
for cases where pdfplumber returns poor text. §12 says:

  "PDF → text: pdfplumber or pymupdf. Fallback to Kimi vision for
   scanned/complex PDFs."

Kimi-vision fallback is a later optimization; not built in Step 3.
"""
from __future__ import annotations

from pathlib import Path

import pdfplumber
import pymupdf


class PDFReadError(Exception):
    pass


MIN_USABLE_CHARS = 500


def parse_pdf_uri(uri: str) -> tuple[Path, tuple[int, int] | None]:
    """Split 'path.pdf#pages=N-M' into (Path, (N, M)).

    Page numbers are 1-based and inclusive. Returns (path, None) if the
    URI has no fragment. A single page uses '#pages=N'.
    """
    if "#" not in uri:
        return Path(uri), None
    path_part, fragment = uri.split("#", 1)
    if not fragment.startswith("pages="):
        raise ValueError(f"Unknown PDF URI fragment: '#{fragment}'")
    spec = fragment[len("pages="):]
    if "-" in spec:
        a, b = spec.split("-", 1)
        start, end = int(a), int(b)
    else:
        start = end = int(spec)
    if start < 1 or end < start:
        raise ValueError(f"Invalid page range: #pages={spec}")
    return Path(path_part), (start, end)


def read_pdf(pdf_path: Path, pages: tuple[int, int] | None = None) -> str:
    """Return the text of the PDF. Optional (start, end) is 1-based inclusive.

    Raises PDFReadError if the file is missing or yields too little text.
    """
    if not pdf_path.exists():
        raise PDFReadError(f"PDF not found: {pdf_path}")

    text = _try_pdfplumber(pdf_path, pages)
    if len(text.strip()) >= MIN_USABLE_CHARS:
        return text

    # Fallback: pymupdf (handles more layouts)
    text = _try_pymupdf(pdf_path, pages)
    if len(text.strip()) >= MIN_USABLE_CHARS:
        return text

    range_hint = f" (pages {pages[0]}-{pages[1]})" if pages else ""
    raise PDFReadError(
        f"PDF '{pdf_path.name}'{range_hint} yielded "
        f"<{MIN_USABLE_CHARS} usable chars. Likely scanned/image-only. "
        f"Kimi-vision fallback not yet implemented."
    )


def _try_pdfplumber(path: Path, pages: tuple[int, int] | None) -> str:
    collected: list[str] = []
    with pdfplumber.open(str(path)) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            if pages and not (pages[0] <= i <= pages[1]):
                continue
            t = page.extract_text() or ""
            if t:
                collected.append(t)
    return "\n\n".join(collected)


def _try_pymupdf(path: Path, pages: tuple[int, int] | None) -> str:
    collected: list[str] = []
    with pymupdf.open(str(path)) as doc:
        for i, page in enumerate(doc, start=1):
            if pages and not (pages[0] <= i <= pages[1]):
                continue
            t = page.get_text("text") or ""
            if t:
                collected.append(t)
    return "\n\n".join(collected)
