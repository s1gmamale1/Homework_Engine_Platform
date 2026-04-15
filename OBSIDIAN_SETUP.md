# Obsidian Team Setup — NETS Vault

Follow these steps once after cloning the repo. Takes ~3 minutes.

## 1. Install Obsidian

Download from [obsidian.md](https://obsidian.md) and install.

## 2. Open the vault

1. Launch Obsidian
2. Click **Open folder as vault**
3. Navigate to your local clone of this repo (`Homework_Engine_Platform/`)
4. Click **Open**

## 3. Trust plugins

Obsidian will prompt: *"This vault contains plugins. Do you trust the author?"*

Click **Trust author and enable plugins**.

The following plugins are pre-configured and will activate automatically:

| Plugin | Purpose |
|--------|---------|
| Templater | Template system for new notes |
| Calendar | Week/day navigation panel |
| Icon Folder | Folder icons in sidebar for visual navigation |
| Terminal | Integrated terminal panel (run scripts from vault) |
| Open in Terminal | Right-click folder → open in external terminal |

## 4. Start here

Open `HOME.md` — it's the central hub with links to all 5 architecture layers, subject families, game mechanics, agents, and research.

## 5. Graph view

Press `Ctrl+G` (or `Cmd+G` on Mac) to open Graph view.

The graph uses **color groups** to visually separate vault layers:

| Color | Group | What it covers |
|-------|-------|---------------|
| Red | Frameworks (Layer 0-4) | UNIFIED-Buzan, Library Framework, Tier Overlay, Grading System |
| Blue | Subject Families (Layer 2) | All family docs + subject frameworks |
| Green | Game Mechanics | Game docs, demos, catalogs |
| Purple | Agents | All agent configs + content producer pipeline |
| Orange | Research | Buzan, curriculum, engagement, compliance |
| Yellow | Narrative | National Pride quotes, facts, strategy |
| Cyan | System Design | UI/UX, system design summaries |

These are pre-configured in `.obsidian/graph.json`. No manual setup needed.

## 6. Key paths

```
HOME.md                          ← Start here
standards/framework/             ← Layers 0, 3, 4 (immutable specs)
standards/library/framework/     ← Layer 1 (Library Framework)
standards/library/subject-family/← Layer 2 (subject frameworks)
standards/library/catalog/       ← Game catalogs
standards/system/games/          ← Game mechanics docs + demos
standards/system/narrative/      ← National Pride data
standards/system/ui-ux/          ← UI/UX spec
agents/                          ← Agent configs
agents/content-producer/         ← Production pipeline (SOUL, SKILLS, SCHEMA)
research/                        ← Background research
scripts/                         ← Build & utility scripts
visuals/                         ← HTML reports, flow diagrams
```

## Notes for the team

- **Do not commit** `.obsidian/workspace.json` or `.obsidian/workspace-mobile.json` — these are personal layout files (already in `.gitignore`)
- **Do commit** any changes to `.obsidian/app.json`, `.obsidian/graph.json`, or plugin configs that should apply to the whole team
- All spec documents in `standards/framework/` are **read-only** unless you own that layer
- Subject frameworks in `standards/library/subject-family/` follow the filter/adapter pattern — read the family doc before writing a new subject framework
- Use `research/INDEX.md` to find background research linked to system nodes
