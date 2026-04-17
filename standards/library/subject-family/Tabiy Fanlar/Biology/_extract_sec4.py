import fitz

PDF_PATH = r'C:\Users\Recruiter\Documents\Homework_Engine_Platform\standards\library\subject-family\Tabiy Fanlar\Biology\5-sinf_biologiya_2020_(elekton_darslikbot).pdf'
OUTPUT = r'C:\Users\Recruiter\Documents\Homework_Engine_Platform\standards\library\subject-family\Tabiy Fanlar\Biology\_section4.txt'

doc = fitz.open(PDF_PATH)

# §4 Hujayra is around pages 17-22 based on the TOC
# Extract pages 17-23 to get the full section
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write("Total pages: " + str(len(doc)) + "\n\n")
    for i in range(16, min(24, len(doc))):
        page = doc[i]
        text = page.get_text()
        imgs = page.get_images()
        f.write(f"=== PAGE {i+1} === (images: {len(imgs)})\n")
        f.write(text.strip())
        f.write("\n\n")

print("Extracted section 4 (Hujayra) pages 17-23")
