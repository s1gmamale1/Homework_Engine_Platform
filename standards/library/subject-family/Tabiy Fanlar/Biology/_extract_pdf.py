import fitz
import os

PDF_PATH = r'C:\Users\Recruiter\Documents\Homework_Engine_Platform\standards\library\subject-family\Tabiy Fanlar\Biology\5-sinf_biologiya_2020_(elekton_darslikbot).pdf'
OUTPUT = r'C:\Users\Recruiter\Documents\Homework_Engine_Platform\standards\library\subject-family\Tabiy Fanlar\Biology\_pdf_extract.txt'

doc = fitz.open(PDF_PATH)
print("Pages:", len(doc))

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(f"Total pages: {len(doc)}\n\n")
    for i in range(min(15, len(doc))):
        page = doc[i]
        text = page.get_text()
        imgs = page.get_images()
        f.write(f"=== PAGE {i+1} === (images: {len(imgs)})\n")
        if text.strip():
            f.write(text[:1500].strip())
        else:
            f.write("[NO TEXT - scanned page or image-only]")
        f.write("\n\n")

print(f"Extracted to: {OUTPUT}")
print(f"File size: {os.path.getsize(OUTPUT)} bytes")
