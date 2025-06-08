#!/bin/bash

echo "🧨 Starting destructive cleanup of your Mac dev environment..."

# === Step 1: Uninstall Xcode Command Line Tools ===
if [ -d "/Library/Developer/CommandLineTools" ]; then
  echo "🧹 Removing Xcode CLI tools..."
  sudo rm -rf /Library/Developer/CommandLineTools
else
  echo "✔️ Xcode CLI tools already removed"
fi

# === Step 2: Clean broken .zprofile lines ===
if [ -f "$HOME/.zprofile" ]; then
  echo "🧽 Cleaning .zprofile of brew and pyenv paths..."
  sed -i '' '/brew shellenv/d' "$HOME/.zprofile"
  sed -i '' '/PYENV_ROOT/d' "$HOME/.zprofile"
  sed -i '' '/pyenv init --path/d' "$HOME/.zprofile"
else
  echo "ℹ️ No .zprofile found"
fi

# === Step 3: Delete old dev folders ===
for folder in "$HOME/code" "$HOME/repos" "$HOME/dev"; do
  if [ -d "$folder" ]; then
    echo "🗑️ Removing old dev folder: $folder"
    rm -rf "$folder"
  fi
done

# === Step 4: Optional — Remove Homebrew, VSCode, dotfiles ===
echo "⚠️ WARNING: This will remove Homebrew and all installed formulas."
read -p "Proceed with Homebrew uninstall? (y/n): " CONFIRM
if [[ "$CONFIRM" == "y" ]]; then
  echo "🧹 Uninstalling Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
else
  echo "⏭️ Skipping Homebrew uninstall"
fi

echo "🗑️ Removing ~/.gitconfig, ~/.npmrc, ~/.zshrc if they exist..."
rm -f ~/.gitconfig ~/.npmrc ~/.zshrc

# === Step 5: Kill VSCode (optional) ===
echo "🗑️ Removing VSCode..."
rm -rf /Applications/Visual\ Studio\ Code.app
rm -rf ~/Library/Application\ Support/Code
rm -rf ~/.vscode

# === Step 6: Clean pyenv if exists ===
if [ -d "$HOME/.pyenv" ]; then
  echo "☠️ Removing pyenv..."
  rm -rf "$HOME/.pyenv"
fi

echo "✅ Destruction complete. Mac is reset for fresh install."