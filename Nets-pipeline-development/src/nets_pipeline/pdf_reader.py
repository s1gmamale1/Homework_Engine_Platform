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


def read_pdf(pdf_path: Path) -> str:
    """Return the full text of the PDF. Raises PDFReadError if unusable."""
    if not pdf_path.exists():
        raise PDFReadError(f"PDF not found: {pdf_path}")

    text = _try_pdfplumber(pdf_path)
    if len(text.strip()) >= MIN_USABLE_CHARS:
        return text

    # Fallback: pymupdf (handles more layouts)
    text = _try_pymupdf(pdf_path)
    if len(text.strip()) >= MIN_USABLE_CHARS:
        return text

    raise PDFReadError(
        f"PDF '{pdf_path.name}' yielded <{MIN_USABLE_CHARS} usable chars. "
        f"Likely scanned/image-only. Kimi-vision fallback not yet implemented."
    )


def _try_pdfplumber(path: Path) -> str:
    pages: list[str] = []
    with pdfplumber.open(str(path)) as pdf:
        for page in pdf.pages:
            t = page.extract_text() or ""
            if t:
                pages.append(t)
    return "\n\n".join(pages)


def _try_pymupdf(path: Path) -> str:
    pages: list[str] = []
    with pymupdf.open(str(path)) as doc:
        for page in doc:
            t = page.get_text("text") or ""
            if t:
                pages.append(t)
    return "\n\n".join(pages)
