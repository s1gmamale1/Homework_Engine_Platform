#!/usr/bin/env bash
# squad-tui.sh — Multi-Agent War Room with Unified MCP Memory
# Agents: Opus, Sonnet, Qwen, Codex, Gemini
# Memory: Shared via Obsidian MCP Server (mcp-config.json)

SESSION="SQUAD"

# Check if tmux is installed
if ! command -v tmux &> /dev/null; then
    echo "Error: tmux is not installed. Please run 'sudo apt install tmux' in WSL."
    exit 1
fi

# 1. Check if session exists, if so, just attach
tmux has-session -t $SESSION 2>/dev/null
if [ $? == 0 ]; then
    tmux attach-session -t $SESSION
    exit 0
fi

# 2. Start the Session and Pane 1 (Top-Left): Claude Opus (Logics)
tmux new-session -d -s $SESSION -n "WarRoom"
tmux send-keys -t $SESSION "claude --model opus --name OPUS_LOGIC --mcp-config mcp-config.json" C-m

# 3. Create Pane 2 (Top-Right): Claude Sonnet (Frontend/UI)
tmux split-window -h -t $SESSION
tmux send-keys -t $SESSION "claude --model sonnet --name SONNET_UI --mcp-config mcp-config.json" C-m

# 4. Create Pane 3 (Bottom-Left): Qwen Coder (Uzbek Content)
tmux select-pane -t 0
tmux split-window -v -t $SESSION
tmux send-keys -t $SESSION "qwen --model qwen-coder --mcp-config mcp-config.json" C-m

# 5. Create Pane 4 (Bottom-Right): Codex / GPT-4o (Integration)
tmux select-pane -t 2
tmux split-window -v -t $SESSION
tmux send-keys -t $SESSION "openclaw --model codex --mcp-config mcp-config.json" C-m

# 6. Create Pane 5 (Full-Width Bottom): Gemini (CEO/Orchestrator)
tmux select-pane -t 1
tmux split-window -v -p 30 -t $SESSION
tmux send-keys -t $SESSION "gemini --model auto" C-m

# 7. Set focus back to Gemini
tmux select-pane -t 4

# Start the session
tmux attach-session -t $SESSION
