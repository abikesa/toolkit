Here you go:

👉 [**Download `clean-dev-env.sh`**](sandbox:/mnt/data/clean-dev-env.sh)

This shell script will **nuke all dev-related tools**—VS Code, user-installed Python, Homebrew, Git credentials, SSH keys, and shell config files—bringing your Mac back to a "just Word and PowerPoint" baseline.

### 🧪 How to Use It:

1. Open Terminal.
2. Navigate to the folder where you downloaded it:

   ```bash
   cd ~/Downloads  # or wherever you saved it
   ```
3. Run the script:

   ```bash
   chmod +x clean-dev-env.sh
   ./clean-dev-env.sh
   ```

Let me know if you want a **safe mode** version (e.g., prompts before each nuke), or if you'd like the inverse: a `.sh` to install VS Code, Git, Python, and clone a repo—like the dev resurrection spell.


## Background 

Exactly—you’ve been cruising on **SSH** the whole time, which is why GitHub Just Worked™ for you. That’s the good life. Now, if you want to **nuke your dev environment** and roll back your Mac to a clean, non-dev, Office-only state—basically make it like it was bought by a humanities major—here’s the full purge.

---

## 🧨 DEV EXORCISM: Return Your Mac to Pre-Code Innocence

This gets rid of:

* Python (custom installs, not system default)
* VS Code
* Git configs
* Homebrew (if installed)
* Any terminal cruft (e.g., `.zshrc`, `.bash_profile`)
* SSH keys
* Any developer SDKs

---

### 🔪 1. Remove VS Code

```bash
rm -rf /Applications/Visual\ Studio\ Code.app
rm -rf ~/.vscode
rm -rf ~/Library/Application\ Support/Code
rm -rf ~/Library/Caches/com.microsoft.VSCode
rm -rf ~/Library/Saved\ Application\ State/com.microsoft.VSCode.savedState
```

> Optionally, delete workspace settings:

```bash
rm -rf ~/Library/Preferences/com.microsoft.VSCode.plist
```

---

### 🐍 2. Remove Python (User-Installed Only)

Do **not** delete macOS system Python (can break things). But if you manually installed Python (via python.org or Homebrew):

Check versions:

```bash
which python3
```

If it shows `/Library/Frameworks/...`, remove with:

```bash
sudo rm -rf /Library/Frameworks/Python.framework
sudo rm -rf /Applications/Python\ 3.*
sudo rm -rf /usr/local/bin/python3
sudo rm -rf /usr/local/bin/pip3
```

Then clean launchers:

```bash
rm -f ~/.local/bin/python3
rm -f ~/.local/bin/pip3
```

---

### 🍺 3. Remove Homebrew (if installed)

Check if installed:

```bash
which brew
```

If so, uninstall:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

---

### 🔑 4. Remove Git Config and Credentials

Clear Git identity and saved credentials:

```bash
rm -f ~/.gitconfig
rm -f ~/.git-credentials
git config --global --unset credential.helper
```

Remove macOS Keychain saved GitHub tokens:

```bash
security delete-generic-password -s "github.com"
```

(Repeat if multiple tokens exist.)

---

### 🕵️ 5. Remove SSH Keys

Careful—this nukes all existing keys.

```bash
rm -rf ~/.ssh
```

(Also removes known hosts, if you want to be *really* clean.)

---

### 🧼 6. Reset Shell Configs

These may have been edited by dev tools. Optional, but recommended:

```bash
rm -f ~/.zshrc
rm -f ~/.bash_profile
rm -f ~/.bashrc
rm -f ~/.profile
```

They’ll regenerate with safe defaults on next login.

---

### 🔍 7. Final Audit: What's Left?

Search manually for dev-related junk:

```bash
ls -a ~ | grep -iE 'python|code|git|brew|venv|node|npm'
```

Then purge what’s unnecessary.

---

### ✅ Post-Cleanup State

Your Mac now behaves like:

* No dev tools were ever installed.
* GitHub who? VS what?
* Just Office, Safari, and vibes.

If you want to make this repeatable, I can script it into a `.sh` file (`clean-dev-env.sh`) and you can drop it into any intern’s laptop like a dev nuke.

Let me know—I'll ship it.
# flick 20250602215535-jky4
# flick 20250603170605-jLkI
# flick 20250603221409-rIiG
