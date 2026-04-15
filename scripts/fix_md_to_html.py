import re

def markdown_to_html(md_path, html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Meta extraction
    meta_match = re.search(r'## Metadata\n\n(.*?)\n---', content, re.DOTALL)
    metadata = {}
    if meta_match:
        rows = meta_match.group(1).strip().split('\n')
        for row in rows:
            if '|' in row and '---' not in row:
                cols = [c.strip() for c in row.split('|') if c.strip()]
                if len(cols) == 2:
                    label = cols[0].replace('**', '')
                    value = cols[1]
                    metadata[label] = value

    # Split into main Phases
    phases = re.split(r'\n(?=## PHASE)', content)
    
    html_sections = ""
    
    for phase in phases:
        phase = phase.strip()
        if not phase or phase.startswith('# NETS') or phase.startswith('## Metadata'):
            continue
            
        phase = re.sub(r'^-{3,}\n', '', phase, flags=re.M)
        lines = phase.split('\n')
        phase_title = lines[0].replace('## ', '').strip()
        phase_body = '\n'.join(lines[1:]).strip()
        
        # 1. Handle PHASE 0-A (Theme Preview) with Panels as Square Boxes
        if "PHASE 0-A" in phase_title:
            panels = re.split(r'\n(?=### Panel)', phase_body)
            preview_intro = ""
            panels_html = ""
            
            for part in panels:
                part = part.strip()
                if not part: continue
                if part.startswith('### Panel'):
                    p_lines = part.split('\n')
                    p_title = p_lines[0].replace('### ', '').strip()
                    p_body = '\n'.join(p_lines[1:]).strip()
                    p_body_html = format_body_text(p_body)
                    
                    panels_html += f"""
                    <div class="info-panel">
                        <div class="panel-header">{p_title}</div>
                        <div class="panel-body">{p_body_html}</div>
                    </div>
                    """
                else:
                    preview_intro += format_body_text(part)
            
            html_sections += f"""
            <section class="dropdown-section">
                <details>
                    <summary>{phase_title}</summary>
                    <div class="content">
                        {preview_intro}
                        <div class="panels-grid">
                            {panels_html}
                        </div>
                    </div>
                </details>
            </section>
            """

        # 2. Handle PHASE 0-B (Flashcards) - already improved
        elif "PHASE 0-B" in phase_title:
            cards = re.split(r'\n(?=### Kartochka)', phase_body)
            flashcards_content = ""
            for card in cards:
                card = card.strip()
                if not card: continue
                card_lines = card.split('\n')
                card_body = '\n'.join(card_lines[1:])
                parts = re.split(r'\*\*.*?(?:fronti|orqasi).*?\*\*', card_body, flags=re.IGNORECASE)
                if len(parts) >= 3:
                    front = parts[1].strip().replace('```', '').strip()
                    back = parts[2].strip().replace('```', '').strip()
                    flashcards_content += f"""
                    <div class="flashcard" onclick="this.classList.toggle('flipped')">
                        <div class="flashcard-inner">
                            <div class="flashcard-front"><div class="card-label">SAVOL</div><div class="card-text">{front.replace('\n', '<br>')}</div></div>
                            <div class="flashcard-back"><div class="card-label">JAVOB</div><div class="card-text">{back.replace('\n', '<br>')}</div></div>
                        </div>
                    </div>
                    """
            html_sections += f"""
            <section class="dropdown-section">
                <details>
                    <summary>{phase_title}</summary>
                    <div class="content">
                        <p style="margin-bottom: 20px; color: var(--secondary-color); text-align: center;">Kartochkani ag'darish uchun ustiga bosing.</p>
                        <div class="flashcards-container">{flashcards_content}</div>
                    </div>
                </details>
            </section>
            """

        # 3. Handle PHASE 1 (Memory Sprint) with Question Formatting
        elif "PHASE 1" in phase_title:
            questions = re.split(r'\n(?=### Savol)', phase_body)
            sprint_intro = ""
            questions_html = ""
            for q_part in questions:
                q_part = q_part.strip()
                if not q_part: continue
                if q_part.startswith('### Savol'):
                    q_lines = q_part.split('\n')
                    q_title = q_lines[0].replace('### ', '').strip()
                    q_body = '\n'.join(q_lines[1:]).strip()
                    
                    # Extract options if any
                    options = re.findall(r'([a-d]\) .*?)(?=\n[a-d]\) |$|\n\n)', q_body, flags=re.S)
                    q_text = re.sub(r'[a-d]\) .*?(\n|$)', '', q_body).strip()
                    
                    # Extract answer and explanation
                    answer_match = re.search(r'Javob: (.*?)\n', q_body)
                    explain_match = re.search(r'Tushuntirish: (.*?)(?=\n\n|$)', q_body, flags=re.S)
                    
                    options_html = ""
                    for opt in options:
                        options_html += f'<div class="quiz-option">{opt}</div>'
                        
                    questions_html += f"""
                    <div class="quiz-item">
                        <div class="quiz-header">{q_title}</div>
                        <div class="quiz-question">{format_body_text(q_text)}</div>
                        <div class="quiz-options">{options_html}</div>
                        <details class="quiz-answer-details">
                            <summary class="quiz-answer-summary">To'g'ri javobni ko'rish</summary>
                            <div class="quiz-answer-content">
                                <strong>Javob:</strong> {answer_match.group(1) if answer_match else 'Aytilmagan'}<br>
                                <strong>Tushuntirish:</strong> {explain_match.group(1) if explain_match else "Izoh yo'q"}
                            </div>
                        </details>
                    </div>
                    """
                else:
                    sprint_intro += format_body_text(q_part)
            
            html_sections += f"""
            <section class="dropdown-section">
                <details>
                    <summary>{phase_title}</summary>
                    <div class="content">
                        {sprint_intro}
                        <div class="quiz-container">{questions_html}</div>
                    </div>
                </details>
            </section>
            """

        # 4. Regular Sections
        else:
            body_html = format_body_text(phase_body)
            html_sections += f"""
            <section class="dropdown-section">
                <details>
                    <summary>{phase_title}</summary>
                    <div class="content">{body_html}</div>
                </details>
            </section>
            """

    html_template = f"""<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NETS Homework - {metadata.get('Fan', 'Matematika')}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #f4f7f9;
            --card-bg: #ffffff;
            --text-color: #2c3e50;
            --primary-color: #2980b9;
            --secondary-color: #7f8c8d;
            --accent-color: #ecf0f1;
            --border-color: #dcdde1;
            --success-color: #27ae60;
            --shadow: 0 4px 12px rgba(0,0,0,0.08);
            --panel-border: #3498db;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Inter', sans-serif;
            line-height: 1.7;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }}
        .container {{ width: 100%; max-width: 950px; }}
        header {{
            text-align: center; margin-bottom: 30px; padding: 40px;
            background: var(--card-bg); border-radius: 20px;
            box-shadow: var(--shadow);
            border-bottom: 8px solid var(--primary-color);
        }}
        h1 {{ color: var(--primary-color); font-size: 2.4rem; margin-bottom: 10px; font-weight: 800; }}
        .subtitle {{ color: var(--secondary-color); font-weight: 500; font-size: 1.2rem; letter-spacing: 1px; }}
        
        .metadata-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 30px; text-align: left; }}
        .metadata-item {{ background: var(--accent-color); padding: 15px; border-radius: 12px; border: 1px solid var(--border-color); }}
        .metadata-label {{ color: var(--secondary-color); font-size: 0.75rem; text-transform: uppercase; font-weight: 700; display: block; margin-bottom: 4px; }}
        .metadata-value {{ font-weight: 700; font-size: 1.05rem; color: var(--text-color); }}
        
        section.dropdown-section {{ margin-bottom: 20px; }}
        details {{ background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 15px; overflow: hidden; transition: all 0.3s ease; }}
        details[open] {{ box-shadow: var(--shadow); border-color: var(--primary-color); }}
        
        summary {{ 
            padding: 22px 30px; cursor: pointer; font-weight: 700; font-size: 1.2rem; 
            color: var(--text-color); list-style: none; display: flex; 
            justify-content: space-between; align-items: center; 
            background: #fff; transition: background 0.2s;
        }}
        summary:hover {{ background: var(--accent-color); }}
        summary::after {{ 
            content: '▼'; font-size: 0.9rem; color: var(--secondary-color); transition: transform 0.3s;
        }}
        details[open] summary {{ border-bottom: 2px solid var(--accent-color); background: var(--accent-color); }}
        details[open] summary::after {{ transform: rotate(180deg); color: var(--primary-color); }}
        
        .content {{ padding: 35px; background: #fff; }}
        
        /* Panel Boxes Styling */
        .panels-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-top: 25px;
        }}
        .info-panel {{
            background: #fff;
            border: 2px solid var(--accent-color);
            border-left: 6px solid var(--panel-border);
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .info-panel:hover {{
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            border-color: var(--panel-border);
        }}
        .panel-header {{
            font-weight: 800;
            font-size: 1.1rem;
            color: var(--primary-color);
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .panel-body {{
            font-size: 0.95rem;
            color: var(--text-color);
        }}

        /* Quiz Sprint Styling */
        .quiz-container {{
            display: flex;
            flex-direction: column;
            gap: 30px;
            margin-top: 20px;
        }}
        .quiz-item {{
            background: var(--bg-color);
            border-radius: 15px;
            padding: 30px;
            border: 1px solid var(--border-color);
        }}
        .quiz-header {{
            font-weight: 800;
            color: var(--secondary-color);
            font-size: 0.85rem;
            text-transform: uppercase;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }}
        .quiz-question {{
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 20px;
            color: var(--text-color);
        }}
        .quiz-options {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
            margin-bottom: 20px;
        }}
        .quiz-option {{
            background: #fff;
            padding: 12px 18px;
            border-radius: 10px;
            border: 1px solid var(--border-color);
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .quiz-option:hover {{
            background: var(--primary-color);
            color: #fff;
            border-color: var(--primary-color);
        }}
        .quiz-answer-details {{
            margin-top: 15px;
            border: none;
            border-radius: 10px;
            background: rgba(39, 174, 96, 0.05);
        }}
        .quiz-answer-summary {{
            padding: 12px 20px;
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--success-color);
            background: transparent;
        }}
        .quiz-answer-content {{
            padding: 0 20px 20px 20px;
            font-size: 0.95rem;
            border: none;
        }}

        /* Flashcards Styling */
        .flashcards-container {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; perspective: 1000px; }}
        .flashcard {{ height: 220px; cursor: pointer; perspective: 1000px; }}
        .flashcard-inner {{ position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; }}
        .flashcard.flipped .flashcard-inner {{ transform: rotateY(180deg); }}
        .flashcard-front, .flashcard-back {{ position: absolute; width: 100%; height: 100%; backface-visibility: hidden; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 25px; border-radius: 16px; border: 2px solid var(--border-color); background: #fff; }}
        .flashcard-back {{ transform: rotateY(180deg); background: var(--accent-color); border-color: var(--primary-color); }}
        .card-label {{ font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 15px; color: var(--secondary-color); }}
        .flashcard-front .card-text {{ font-size: 1.1rem; font-weight: 700; color: var(--primary-color); }}
        .flashcard-back .card-text {{ font-size: 0.95rem; color: var(--text-color); }}

        /* General Typography */
        h3 {{ color: var(--primary-color); margin-top: 30px; margin-bottom: 15px; font-size: 1.3rem; font-weight: 700; }}
        p {{ margin-bottom: 18px; }}
        blockquote {{ border-left: 6px solid var(--primary-color); padding: 18px 28px; background: var(--accent-color); font-style: italic; margin: 25px 0; border-radius: 0 15px 15px 0; }}
        pre {{ background: #1e1e1e; color: #dcdcdc; padding: 22px; border-radius: 12px; overflow-x: auto; margin: 20px 0; font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; line-height: 1.6; white-space: pre-wrap; }}
        table {{ width: 100%; border-collapse: collapse; margin: 25px 0; border: 1px solid var(--border-color); border-radius: 10px; overflow: hidden; }}
        th, td {{ padding: 15px 20px; text-align: left; border-bottom: 1px solid var(--border-color); }}
        th {{ background: var(--accent-color); color: var(--primary-color); font-weight: 700; font-size: 0.85rem; text-transform: uppercase; }}
        hr {{ border: 0; border-top: 2px solid var(--accent-color); margin: 35px 0; }}
        .highlight {{ color: var(--primary-color); font-weight: 700; }}

        .btn-start {{ 
            display: block; width: 100%; padding: 22px; background: var(--primary-color); 
            color: #fff; text-align: center; text-decoration: none; font-weight: 700; 
            text-transform: uppercase; letter-spacing: 2px; border-radius: 15px; 
            margin-top: 40px; transition: all 0.3s; border: none; cursor: pointer;
            box-shadow: 0 5px 15px rgba(41, 128, 185, 0.4); font-size: 1.1rem;
        }}
        .btn-start:hover {{ background: #21618c; transform: translateY(-3px); box-shadow: 0 8px 20px rgba(41, 128, 185, 0.5); }}
        
        .status-footer {{ margin-top: 60px; padding: 30px; border-top: 1px solid var(--border-color); font-size: 0.9rem; color: var(--secondary-color); text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>NETS Homework Session</h1>
            <p class="subtitle">{metadata.get('Fan', 'MATEMATIKA')} — GRADE {metadata.get('Sinf', '5')}</p>
            <div class="metadata-grid">
                <div class="metadata-item"><span class="metadata-label">Mavzu</span><span class="metadata-value">{metadata.get("Bo'lim", '1.3. 10 milliongacha')}</span></div>
                <div class="metadata-item"><span class="metadata-label">Bob</span><span class="metadata-value">{metadata.get('Bob', '1')}</span></div>
                <div class="metadata-item"><span class="metadata-label">Standard</span><span class="metadata-value">{metadata.get('Standard kodi', 'UZ-MAT-5')}</span></div>
                <div class="metadata-item"><span class="metadata-label">Boss HP</span><span class="metadata-value">{metadata.get('Boss HP', '80')} HP</span></div>
            </div>
        </header>
        {html_sections}
        <button class="btn-start">MENING UY VAZIFAMNI BOSHLASH 🚀</button>
        <div class="status-footer">
            <p>Status: Tamatdi ✅ | Sana: 2026-04-15</p>
            <p>NETS Homework Engine Specification v2.0</p>
        </div>
    </div>
</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_template)

def format_body_text(text):
    if not text: return ""
    # Tables
    text = re.sub(r'\|(.*?)\|\n\|[- |]+\|\n((?:\|.*?\|\n?)*)', table_repl, text, flags=re.S)
    # Lists
    text = re.sub(r'^- (.*)', r'<li>\1</li>', text, flags=re.M)
    text = re.sub(r'((?:<li>.*?</li>\n?)+)', r'<ul>\1</ul>', text, flags=re.S)
    # Code
    text = re.sub(r'```(.*?)```', r'<pre>\1</pre>', text, flags=re.DOTALL)
    # Quotes
    text = re.sub(r'>(.*?)(?:\n|$)', r'<blockquote>\1</blockquote>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Newlines to BR
    text = text.replace('\n', '<br>')
    # Fix extra BRs inside block elements
    text = text.replace('</blockquote><br>', '</blockquote>')
    text = text.replace('</ul><br>', '</ul>')
    text = text.replace('</pre><br>', '</pre>')
    text = text.replace('</div><br>', '</div>')
    return text

def table_repl(match):
    header = match.group(1).strip()
    rows = match.group(2).strip().split('\n')
    
    h_cols = [c.strip() for c in header.split('|') if c.strip()]
    h_html = "".join([f"<th>{c}</th>" for c in h_cols])
    
    r_html = ""
    for r in rows:
        r_cols = [c.strip() for c in r.split('|') if c.strip()]
        r_html += "<tr>" + "".join([f"<td>{c}</td>" for c in r_cols]) + "</tr>"
        
    return f"<table><thead><tr>{h_html}</tr></thead><tbody>{r_html}</tbody></table>"

if __name__ == "__main__":
    markdown_to_html('Homeworks/Matematika_Grade5_Ch1S1.3_uz.md', 'Homeworks/Matematika_Grade5_Ch1S1.3_uz.html')
