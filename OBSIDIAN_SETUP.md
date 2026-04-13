# Obsidian Team Setup — NETS Vault

Follow these steps once after cloning the repo. Takes ~3 minutes.

## 1. Install Obsidian

Download from [obsidian.md](https://obsidian.md) and install.

## 2. Open the vault

1. Launch Obsidian
2. Click **Open folder as vault**
3. Navigate to your local clone of this repo (`Sigma_Edu_3000/`)
4. Click **Open**

## 3. Trust plugins

Obsidian will prompt: *"This vault contains plugins. Do you trust the author?"*

Click **Trust author and enable plugins**.

The following plugins are pre-configured and will activate automatically:

| Plugin | Purpose |
|--------|---------|
| Templater | Template system for new notes |
| Calendar | Week/day navigation panel |
| Icon Folder | Folder icons in sidebar |
| Terminal | Integrated terminal panel |
| Open in Terminal | Right-click → open folder in terminal |

## 4. Start here

Open `HOME.md` — it's the central hub with links to all subsystems.

Use `Ctrl+G` (Graph view) to see the full knowledge map.

## Notes for the team

- **Do not commit** `.obsidian/workspace.json` or `.obsidian/workspace-mobile.json` — these are personal layout files (already in `.gitignore`)
- **Do commit** any changes to `.obsidian/app.json`, `.obsidian/graph.json`, or plugin configs that should apply to the whole team
- All spec documents are in `standards/` — treat them as read-only unless you are the owner of that subsystem
