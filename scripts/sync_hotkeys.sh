#!/bin/bash
# Pull latest changes from dev branch
config pull origin dev

# Reload xbindkeys if it's not running
if ! pgrep xbindkeys >/dev/null; then
    xbindkeys
fi
