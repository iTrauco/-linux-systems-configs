#!/bin/bash
set -euo pipefail

echo "Starting hotkey setup..."

# Check and install required packages
if ! command -v xbindkeys >/dev/null 2>&1; then
    echo "xbindkeys not found. Installing required packages..."
    sudo apt-get update
    sudo apt-get install -y xbindkeys
else
    echo "xbindkeys already installed."
fi

# Create xbindkeys config if it doesn't exist
if [ ! -f ~/.xbindkeysrc ]; then
    echo "Creating initial xbindkeys configuration..."
    xbindkeys --defaults > ~/.xbindkeysrc
fi

# Backup existing config
cp ~/.xbindkeysrc ~/.xbindkeysrc.backup

echo "Appending custom keybindings..."
# First remove any existing bindings for our scripts (to avoid duplicates)
grep -v "claude\|openai" ~/.xbindkeysrc > ~/.xbindkeysrc.tmp
mv ~/.xbindkeysrc.tmp ~/.xbindkeysrc

# Now append our custom keybindings
cat >> ~/.xbindkeysrc << 'KEYBINDINGS'

# Custom AI Script Bindings
# Control + Alt + 1 for claude1.sh
"~/scripts/claude1.sh"
  Control+Alt + 1
# Control + Alt + 2 for claude2.sh
"~/scripts/claude2.sh"
  Control+Alt + 2
# Control + Alt + 3 for claude3.sh
"~/scripts/claude3.sh"
  Control+Alt + 3
# Control + Alt + 4 for claude4.sh
"~/scripts/claude4.sh"
  Control+Alt + 4
# Control + Alt + 5 for claude-personal.sh
"~/scripts/claude-personal.sh"
  Control+Alt + 5
# Control + Alt + 6 for claude-dev.sh
"~/scripts/claude-dev.sh"
  Control+Alt + 6
# Control + Alt + 7 for openai-personal.sh
"~/scripts/openai-personal.sh"
  Control+Alt + 7
KEYBINDINGS

# Start xbindkeys
echo "Starting xbindkeys..."
killall xbindkeys 2>/dev/null || true
xbindkeys

echo
echo "Setup complete! Hotkeys are configured."
