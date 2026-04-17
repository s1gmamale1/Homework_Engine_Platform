import fitz
import re

PDF_PATH = r'C:\Users\Recruiter\Documents\Homework_Engine_Platform\standards\library\subject-family\Tabiy Fanlar\Biology\5-sinf_biologiya_2020_(elekton_darslikbot).pdf'
OUTPUT = r'C:\Users\Recruiter\Documents\Homework_Engine_Platform\standards\library\subject-family\Tabiy Fanlar\Biology\_full_toc.txt'

doc = fitz.open(PDF_PATH)

sections = []
for i in range(len(doc)):
    page = doc[i]
    text = page.get_text()
    lines = text.strip().split('\n')
    for line in lines:
        line = line.strip()
        # Match chapter headers: I BOB, II BOB, etc.
        if re.match(r'^[IVX]+ BOB\.', line):
            sections.append(f'PAGE {i+1}: *** {line} ***')
        # Match section headers: §1., §2., etc.
        elif re.match(r'^\d+-§', line) or re.match(r'^§ \d+', line):
            sections.append(f'  PAGE {i+1}: {line}')
        # Match lab/practice headers
        elif 'laboratoriya mashg' in line.lower() or 'amaliy mashg' in line.lower():
            if len(line) < 80:
                sections.append(f'    PAGE {i+1}: {line}')

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(f"Total pages: {len(doc)}\n")
    f.write(f"Found {len(sections)} sections:\n\n")
    for s in sections:
        f.write(s + '\n')

print(f"Found {len(sections)} sections across {len(doc)} pages")
for s in sections:
    print(s)
