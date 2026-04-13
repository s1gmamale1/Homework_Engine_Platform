# Notion-Video-Lesson Tools — Quick Reference

**Source of truth:** `C:/Users/DaddysHere/Documents/Notion---Video-Lesson/TOOLS_REFERENCE.md` (513 lines).
**Use this file first.** Only re-read the source if I need a method signature not listed here or if something behaves unexpectedly.

**Project root:** `C:/Users/DaddysHere/Documents/Notion---Video-Lesson/`
**Run commands from there** so the `tools.*` imports resolve.

---

## When to reach for these tools

- Pulling textbook chapter content from Notion → use as input to NETS homework generation
- Writing NETS-generated content (refined text, prompts, scenes) back to Notion sub-pages
- Downloading textbook PDFs from Notion to render or extract pages
- Coordinating long video-generation runs via the SQLite task queue
- Generating images (Whisk) and videos (Grok) via browser automation

**Do NOT edit code in Notion---Video-Lesson/** unless explicitly asked or fixing a bug.

---

## The 3-stage pipeline

| Stage | What happens | Key tools |
|---|---|---|
| **NOTION MODE** | Scan workspace, download PDFs, create chapter pages + 13 sub-pages each | NotionNavigator, NotionPageCreator, PDFHandler |
| **SCRIPT MODE** | Extract chapter text, write scenes/prompts/manifest, upload back to Notion | NotionExtractor, NotionContentWriter, Scene/Script tools |
| **MEDIA MODE** | Generate images (Whisk), videos (Grok), zip + upload to Notion | Browser automation, upload-media CLI |

All stages claim/complete tasks via PipelineDB.

---

## Python Imports — the 7 things I'll import most

```python
from tools.notion.db import PipelineDB
from tools.notion.navigator import NotionNavigator
from tools.notion.extractor import NotionExtractor
from tools.notion.content_writer import NotionContentWriter
from tools.notion.pdf_handler import PDFHandler
from tools.notion.page_creator import NotionPageCreator
from tools.script.scenes import save_scenes, load_scenes
```

---

## Most common patterns (copy-paste-ready)

### Find a chapter and read its refined text

```python
nav = NotionNavigator()
ch = nav.find_chapter(7, "uz", "Geometriya", 1)  # grade, lang, subject, chapter_num
extractor = NotionExtractor()
result = extractor.extract_chapter(7, "uz", "Geometriya", 1)
text = result["refined_text"] or result["raw_text"]
```

### Get sub-page IDs by type

```python
subpages = nav.get_chapter_subpages(ch["id"])
sp_map = {sp["type_hint"]: sp["id"] for sp in subpages}
text_original_id = sp_map["text_original"]
images_id        = sp_map["images"]
```

**type_hint values:** `text_original`, `text_refined`, `prompt`, `images`, `video`, `audio`, `final_video`, `lesson_files`, `quizlet`, `homework`, `lesson_plan`, `teacher_prep`, `prezi`, `unknown`

### Write refined text to a sub-page (clears existing first)

```python
writer = NotionContentWriter(client=nav.client)
writer.write_with_clear(refined_id, refined_text, text_type="refined", chapter_title="1-mavzu")
```

### Download a textbook PDF

```python
handler = PDFHandler(client=nav.client)
subject = nav.find_subject(7, "uz", "Geometriya")
pdf_bytes, filename = handler.download_pdf_from_notion(subject["id"])
```

### Upload any file (≤20 MB) to a Notion page

```python
upload_id = nav.client.upload_file("/path/to/file.zip")
block = nav.client.make_file_upload_block(upload_id, "file.zip")
nav.client.append_block_children(page_id, [block])
```

### Claim/complete tasks (worker pattern)

```python
db = PipelineDB()  # connects to brain/pipeline.db
task = db.claim_task("EXTRACT", "worker_1", grade=7, language="uz")
# ... do work ...
db.complete_task(task["id"], "worker_1")  # advances to next stage
# on failure:
db.fail_task(task["id"], "PDF page unreadable", "worker_1")  # auto-retries up to 3x
```

---

## CLI cheat-sheet (run from `Notion---Video-Lesson/` root)

```bash
# Pipeline management
python -m tools.notion init-db
python -m tools.notion db-stats

# Browse Notion structure
python -m tools.notion subjects 7 uz
python -m tools.notion chapters 7 uz "Geometriya"
python -m tools.notion status   7 uz "Geometriya" 3        # check sub-page status

# Read content
python -m tools.notion extract 7 uz "Geometriya" 3
python -m tools.notion read    7 uz "Geometriya" 3 text_refined

# Write/upload to a sub-page
python -m tools.notion write   7 uz "Geometriya" 1 text_original brain/.../chapter_01.txt
python -m tools.notion write   7 uz "Geometriya" 1 prompt          brain/.../scenes.json
python -m tools.notion upload-media 7 uz "Geometriya" 1            # zips scenes/*/image.png + video.mp4

# PDFs
python -m tools.notion download-pdf 7 uz "Geometriya"
# Note: download-pdf now recurses into child pages for multi-part subjects (e.g. 1-qism/2-qism);
# saves all PDFs found, skips files that already exist on disk.

# Chapter/sub-page creation (idempotent)
python -m tools.notion init-subject    7 uz "Geometriya" 26
python -m tools.notion init-subject    7 uz "Geometriya" --chapters-file chapters.json
python -m tools.notion create-chapters 7 uz "Geometriya"

# Script mode (filesystem)
python -m tools.script scenes         7 uz "Geometriya" 1
python -m tools.script scene-status   7 uz "Geometriya" 1
python -m tools.script scene-status   7 uz "Geometriya" 1 5
python -m tools.script prompts        7 uz "Geometriya" 1 5
python -m tools.script chapter-status 7 uz "Geometriya" 1
python -m tools.script manifest       7 uz "Geometriya" 1

# Browser automation (image + video gen)
python -m tools.browser save-session    whisk  account@gmail.com
python -m tools.browser save-session    grok   account@gmail.com
python -m tools.browser verify-session  whisk  account@gmail.com
python -m tools.browser generate-image  account@gmail.com prompt.txt out.png
python -m tools.browser generate-video  account@gmail.com prompt.txt out.mp4 --image=src.png
python -m tools.browser batch-images    scenes_folder/    account@gmail.com
python -m tools.browser batch-videos    scenes_folder/    account@gmail.com
python -m tools.browser worker 1                          # headless worker
python -m tools.browser worker 2 --headless=false         # debug visible
```

---

## Brain filesystem layout

```
brain/
  pipeline.db                                # task queue
  config/notion_map.json                     # workspace map
  {grade}/{lang}/                            # e.g. 7/uz/
    inventory.json
    subjects/{subject}/                      # subjects/geometriya/
      textbook.pdf
      raw_text/chapter_01.txt
      refined_text/chapter_01.md
      scripts/chapter_01/
        video_script.md
        scenes.json
        assembly_manifest.json
        scenes/01/
          image_prompt.txt
          video_prompt.txt
          narration.txt
          image.png      # generated
          video.mp4      # generated
  accounts/sessions/{service}/{email}/
    state.json
    chrome_profile/
```

**Naming rules:** grade = int (`7`), lang = `uz`/`ru`, subject = lowercase_underscored (`jahon_tarixi`), chapter = zero-padded (`chapter_01`), scene = zero-padded dir (`01/`).

---

## Constraints I must respect

| Limit | Value | Handled by |
|---|---|---|
| Notion API rate | 3 req/sec | auto-throttled in `client.py` |
| Notion rich text | 2,000 chars/segment | auto-chunked |
| Notion block append | 100 blocks/call | auto-batched |
| Notion file upload | **20 MB max** | `upload-media` splits at 19 MB |
| Browser instances | **4 max** total | Manager allocates |
| Whisk accounts | rotate every 2h | Manager coordinates |
| Grok accounts | rotate every 10-15 generations | Manager coordinates |
| Grok video gen | **2-5 min/video** | the bottleneck — plan accordingly |
| RAM budget | 16 GB | macOS ~3GB + 4 browsers ~6GB |
| PipelineDB | SQLite WAL mode | thread-safe for concurrent workers |

---

## Tool × Mode matrix

| Tool | NOTION | SCRIPT | MEDIA |
|---|:-:|:-:|:-:|
| PipelineDB | ✓ | ✓ | ✓ |
| NotionNavigator | ✓ | ✓ | ✓ |
| NotionExtractor | check | read | — |
| NotionContentWriter | — | upload | — |
| PDFHandler | download | render | — |
| NotionPageCreator | ✓ | — | — |
| Scene/Script tools | — | save | load |
| Browser (Whisk) | — | — | images |
| Browser (Grok) | — | — | videos |
| upload-media CLI | — | — | ✓ |
| write CLI | — | upload | — |

---

## Browser CSS selectors (will break when UIs update)

Defined in `tools/browser/config.py`:

- **Whisk:** `textarea`, `button:has-text("Generate")`, `img[src*="generated"]`, `button:has-text("Download")`
- **Grok:** `textarea`, `button:has-text("Imagine")`, `button:has-text("Video")`, `input[type="file"]`, `video`, `button:has-text("Download")`

When broken: run with `--headless=false`, inspect, update `config.py`.

---

## When to re-read the full TOOLS_REFERENCE.md

- I need a method signature not listed here (rare — most are above)
- Something behaves differently than this doc says
- New tool added to the project
- Debugging an obscure error
