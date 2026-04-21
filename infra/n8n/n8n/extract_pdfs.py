import fitz  # pymupdf
import os

books_dir = r"D:\Class A Education\Books"

for root, dirs, files in os.walk(books_dir):
    for f in files:
        if f.endswith(".pdf"):
            pdf_path = os.path.join(root, f)
            txt_path = pdf_path.replace(".pdf", ".txt")
            try:
                doc = fitz.open(pdf_path)
                text = "\n".join([page.get_text() for page in doc])
                with open(txt_path, "w", encoding="utf-8") as out:
                    out.write(text)
                print(f"OK: {txt_path}")
            except Exception as e:
                print(f"FAIL: {pdf_path} — {e}")
