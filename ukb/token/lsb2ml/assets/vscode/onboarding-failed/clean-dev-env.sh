# Creating a shell script that uninstalls common developer tools and resets config files

script_content = """#!/bin/bash

echo "🚨 WARNING: This script will remove dev tools and reset your environment. Proceeding in 5 seconds..."
sleep 5

# Remove VS Code
echo "Removing VS Code..."
rm -rf /Applications/Visual\\ Studio\\ Code.app
rm -rf ~/.vscode
rm -rf ~/Library/Application\\ Support/Code
rm -rf ~/Library/Caches/com.microsoft.VSCode
rm -rf ~/Library/Saved\\ Application\\ State/com.microsoft.VSCode.savedState
rm -rf ~/Library/Preferences/com.microsoft.VSCode.plist

# Remove user-installed Python (NOT system Python)
echo "Removing user-installed Python..."
sudo rm -rf /Library/Frameworks/Python.framework
sudo rm -rf /Applications/Python\\ 3.*
sudo rm -f /usr/local/bin/python3
sudo rm -f /usr/local/bin/pip3
rm -f ~/.local/bin/python3
rm -f ~/.local/bin/pip3

# Remove Homebrew
echo "Removing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"

# Remove Git config and credentials
echo "Removing Git config..."
rm -f ~/.gitconfig
rm -f ~/.git-credentials
git config --global --unset credential.helper
security delete-generic-password -s "github.com" 2>/dev/null

# Remove SSH keys
echo "Removing SSH keys..."
rm -rf ~/.ssh

# Reset shell configs
echo "Resetting shell configs..."
rm -f ~/.zshrc
rm -f ~/.bash_profile
rm -f ~/.bashrc
rm -f ~/.profile

echo "🧼 Developer environment cleanup complete!"
"""

# Save to a file
script_path = "/mnt/data/clean-dev-env.sh"
with open(script_path, "w") as file:
    file.write(script_content)

# Make it executable
import os
os.chmod(script_path, 0o755)

script_path
