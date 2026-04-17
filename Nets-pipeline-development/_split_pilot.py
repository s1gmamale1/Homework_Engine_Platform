"""One-off helper — extracts a page range from the Biology G5 PDF as a
standalone PDF for pilot testing. After this pilot works, we'll write a
proper splitter that uses _full_toc.txt to produce all 18 sections.
"""
from pathlib import Path

import pymupdf

SRC = Path(r"C:\Users\Recruiter\Documents\Homework_Engine_Platform\textbooks\biology\5\uz\5-sinf_biologiya_2020_(elekton_darslikbot).pdf")
OUT_DIR = SRC.parent

# Section 1: §1. Biologiya — hayot haqidagi fan. Pages 5..8 (PyMuPDF is 0-indexed).
# Per _full_toc.txt: §1 starts around page 5, §2 at page 9.
sections = [
    ("01_biologiya-hayot-haqidagi-fan", 4, 8),   # pages 5-9 in human numbering
]

with pymupdf.open(str(SRC)) as doc:
    for name, start, end in sections:
        out_path = OUT_DIR / f"biology_G5_uz_sec{name}.pdf"
        with pymupdf.open() as new_doc:
            new_doc.insert_pdf(doc, from_page=start, to_page=end)
            new_doc.save(str(out_path))
        print(f"wrote {out_path} ({end - start + 1} pages)")
