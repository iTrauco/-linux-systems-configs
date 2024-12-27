#!/bin/bash

# List of aliases to create trigger scripts for
aliases=("claude1" "claude2" "claude3" "claude4" "claude-personal" "claude-dev" "openai-personal")

# Create the ~/scripts directory if it doesn't exist
mkdir -p ~/scripts

# Create a script for each alias
echo "Creating trigger scripts in ~/scripts/..."
for alias_name in "${aliases[@]}"; do
    script_path=~/scripts/"$alias_name".sh
    echo -e "#!/bin/bash\nsource ~/.zshrc\n$alias_name" > "$script_path"
    chmod +x "$script_path"
    echo "Created and made executable: $script_path"
done

# Output instructions for configuring hotkeys
echo -e "\nTo configure XFCE hotkeys, use the following commands:"
for alias_name in "${aliases[@]}"; do
    echo "Assign ~/scripts/$alias_name.sh to a hotkey in XFCE."
done

