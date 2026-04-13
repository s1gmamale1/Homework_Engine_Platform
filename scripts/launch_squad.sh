#!/usr/bin/env bash
# launch_squad.sh — 5-Agent TUI for the NETS Squad
# Models: Claude Opus, Claude Sonnet, Qwen-Coder, Codex, Gemini Auto

SESSION_NAME="NETS_SQUAD"

# Check if tmux session already exists
tmux has-session -t $SESSION_NAME 2>/dev/null

if [ $? != 0 ]; then
  # 1. Start session with Pane 1: Claude Opus
  tmux new-session -d -s $SESSION_NAME -n "Squad_Alpha"
  tmux send-keys -t $SESSION_NAME "claude --model opus" C-m

  # 2. Create right column
  tmux split-window -h -t $SESSION_NAME
  
  # Pane 2 (Top Right): Claude Sonnet
  tmux send-keys -t $SESSION_NAME:0.1 "claude --model sonnet" C-m

  # 3. Split Left Column (Bottom Left quadrant)
  tmux select-pane -t 0
  tmux split-window -v -t $SESSION_NAME
  # Pane 3: Qwen-Coder
  tmux send-keys -t $SESSION_NAME:0.1 "qwen --model qwen-coder" C-m

  # 4. Split Right Column (Bottom Right quadrant)
  tmux select-pane -t 2
  tmux split-window -v -t $SESSION_NAME
  # Pane 4: Codex (via OpenClaw)
  tmux send-keys -t $SESSION_NAME:0.3 "openclaw --model codex" C-m

  # 5. Create a dedicated full-width bottom pane for the CEO
  # Split the entire window horizontally at the bottom
  tmux select-pane -t 1
  tmux split-window -v -p 30 -t $SESSION_NAME
  # Pane 5: Gemini Auto (Orchestrator)
  tmux send-keys -t $SESSION_NAME "gemini --model auto" C-m

  # Set initial focus back to the Orchestrator
  tmux select-pane -t 4
fi

# Attach to the session
tmux attach-session -t $SESSION_NAME
