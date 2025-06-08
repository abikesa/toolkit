
# 🧭 Ukubona Internship Onboarding Plan – *Paul Luswata*

**Phase: Behavioral Health Data Research | Status: Pre-PhD | System: Windows | Internship: Unpaid**

---

## 🌱 1. **Ukuvula** – *Opening the Environment*

### 🪟 Windows Setup

* ✅ Install [Windows Subsystem for Linux (WSL2)](https://learn.microsoft.com/en-us/windows/wsl/install)
* ✅ Install [Ubuntu 22.04 LTS via Microsoft Store](https://apps.microsoft.com/store/detail/ubuntu-22041-lts/9PN20MSR04DW)
* ✅ Launch WSL + update packages:

  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

### 📦 Essential Tools

* ✅ [Install Git for Windows](https://git-scm.com/)
* ✅ [Install Visual Studio Code](https://code.visualstudio.com/)
* ✅ Install WSL Extension inside VS Code
* ✅ Enable GitHub Copilot if available

---

## 🌀 2. **Ukuzula** – *Roaming the Ecosystem*

### 🔑 GitHub & SSH

* ✅ Create GitHub account
* ✅ Generate SSH keys in WSL:

  ```bash
  ssh-keygen -t ed25519 -C "paul@email.com"
  cat ~/.ssh/id_ed25519.pub
  ```
* ✅ Add SSH key to GitHub: [github.com/settings/keys](https://github.com/settings/keys)

### 🧪 Git Fluency

* Practice `git add`, `git commit`, `git push`, `git status`, `git pull`
* Clone your Ukubona repo via SSH:

  ```bash
  git clone git@github.com:ukubona/your-path.git
  ```

---

## 📚 3. **Ukusoma** – *Reading the Symbols*

### 📊 Python Environment

* ✅ Install `pyenv` + `pyenv-virtualenv` in WSL:

  ```bash
  curl https://pyenv.run | bash
  ```
* ✅ Add to `.bashrc`:

  ```bash
  export PATH="$HOME/.pyenv/bin:$PATH"
  eval "$(pyenv init --path)"
  eval "$(pyenv virtualenv-init -)"
  ```
* ✅ Install Python version + create env:

  ```bash
  pyenv install 3.11.12
  pyenv virtualenv 3.11.12 myenv
  pyenv activate myenv
  ```

### 🧰 Install Python Tools

* ✅ `pip install pandas matplotlib seaborn plotly jupyter`
* ✅ Optional: `pip install nbconvert scikit-learn`

---

## 👁️ 4. **Ukubona** – *Seeing the Data*

### 🔬 Project: Behavioral Health Hypothesis

* Develop a reproducible **hypothesis-driven analysis**
* Identify public datasets (e.g. [BRFSS](https://www.cdc.gov/brfss/), [HCUP](https://www.hcup-us.ahrq.gov/), [NSDUH](https://www.samhsa.gov/data/data-we-collect/nsduh-national-survey-drug-use-and-health))
* Focus on questions like:

  * “What social determinants correlate with behavioral health burden?”
  * “Can we model hospital readmissions using public data?”

### 📈 Build + Publish

* Analyze in Python
* Export image (`.jpeg`) of final chart
* Add to personal HTML GitHub Pages site
* Commit & push:

  ```bash
  git add .
  git commit -m "Behavioral health analysis: first findings"
  git push
  ```

---

## 🌸 5. **Ukuvela** – *Becoming a Contributor*

### 📝 Writing + Publication

* Co-author a short 4–5 page working paper
* Embed visuals from GitHub
* Submit to a preprint server (e.g., [medRxiv](https://www.medrxiv.org/), [SSRN](https://www.ssrn.com/index.cfm/en/), or [ResearchGate](https://www.researchgate.net/))

### 🧭 Workplan Tracker

* Setup a public or internal `tracker.md` with:

  * 🔘 Tasks
  * 📅 Deadlines
  * ✅ Milestones
* Encourage him to own his domain: GitHub Issues + Markdown PRs

---

## 🧠 Meta: Training the Analyst Mind

> **Goal**: Help him internalize the epistemic sequence—question, data, code, output, and story—not just as work, but as a recursive ritual.

Frame everything through the dual lens of:

* 📈 *What signal are we extracting?*
* 🧠 *What do we now know differently because of this?*

---

Let me know if you want this as a `.md`, `.pdf`, or prefilled GitHub repo. I can generate a `tracker.md` or a Codespaces-compatible `.devcontainer` too.
# flick 20250530033033-jC3W
# flick 20250602174424-5yWZ
# flick 20250602214625-5hny
# flick 20250602220149-w5Z3
# flick 20250603011046-fnNm
# flick 20250603210408-3Khv
# flick 20250603220330-Ifsj
