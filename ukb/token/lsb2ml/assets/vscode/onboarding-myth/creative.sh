#!/bin/bash

echo "🌱 Rebuilding Ukubona Dev Environment..."

# === 0. XCODE CLI CHECK ===
if ! xcode-select -p &>/dev/null; then
  echo "❌ Xcode CLI tools not found. Run: xcode-select --install"
  exit 1
fi

# === 1. INSTALL HOMEBREW IF NEEDED ===
if ! command -v brew &>/dev/null; then
  echo "🍺 Installing Homebrew..."
  NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> "$HOME/.zprofile"
  eval "$(/opt/homebrew/bin/brew shellenv)"
else
  echo "✅ Homebrew already installed."
fi

# === 2. VERIFY HOMEBREW ===
if ! command -v brew &>/dev/null; then
  echo "❌ Homebrew install failed"
  exit 1
fi

# === 3. INSTALL DEV TOOLS ===
echo "🔨 Installing Git, pyenv, Node.js, xz, VSCode..."
brew install git pyenv node xz
brew install --cask visual-studio-code

# === 4. PYENV SETUP ===
PYTHON_VERSION="3.11.9"
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv &>/dev/null; then
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"

  echo "🐍 Installing Python $PYTHON_VERSION (if needed)..."
  env PATH="$(brew --prefix xz)/bin:$PATH" \
      LDFLAGS="-L$(brew --prefix xz)/lib" \
      CPPFLAGS="-I$(brew --prefix xz)/include" \
      pyenv install $PYTHON_VERSION --skip-existing

  pyenv global $PYTHON_VERSION
else
  echo "❌ pyenv not found even after install"
  exit 1
fi

# === 5. SHELL CONFIG PERSISTENCE ===
echo "🛠️ Ensuring shell config has pyenv and brew settings..."

grep -q 'brew shellenv' ~/.zprofile || echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
grep -q 'PYENV_ROOT' ~/.zprofile || echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
grep -q 'pyenv init --path' ~/.zprofile || echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
grep -q 'pyenv init -' ~/.zshrc || echo 'eval "$(pyenv init -)"' >> ~/.zshrc
grep -q 'pyenv virtualenv-init' ~/.zshrc || echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# === 6. VERIFY TOOLS ===
echo "🧪 Verifying installations..."
echo -n "Git: "; git --version
echo -n "Python: "; python --version
echo -n "Node: "; node --version
echo -n "VSCode: "; command -v code &>/dev/null && code --version || echo "❌ VSCode not found"

# === 7. WORKSPACE SETUP ===
mkdir -p "$HOME/code"
cd "$HOME/code"
echo "📁 Workspace created at ~/code"

# === 8. DONE ===
echo "✅ Ukubona creative dev environment is ready."
echo "🔁 Please restart your terminal or run: source ~/.zshrc"
