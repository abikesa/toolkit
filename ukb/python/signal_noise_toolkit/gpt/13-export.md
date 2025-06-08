Perfect. Since you’re ready to go all in, here’s the plan to add everything—**bonus features**, **CLI filters**, **Markdown/HTML export**, and a **local API**—step by step.

---

## ✅ Step 1: Add CLI Export Features

You’ve already got the CLI working. Let’s make sure the code supports output to Markdown, HTML, or a nice terminal table.

### ✅ You're Done With:

`main.py` — already has export modes for `table`, `md`, and `html`.

You can test it again:

```bash
python3 main.py --layer symbolic --status done --format html
```

---

## ✅ Step 2: Add Script to List Tasks by Due Date

### 📄 Create: `scripts/list_by_due.py`

Paste this into a **new file** at: `signal_noise_toolkit/scripts/list_by_due.py`

```python
import yaml
from pathlib import Path
from tabulate import tabulate
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "layers.yml"

def load_layers():
    with open(DATA_PATH, "r") as f:
        return yaml.safe_load(f)["layers"]

def all_tasks_sorted():
    tasks = []
    for layer in load_layers():
        for task in layer.get("example_tasks", []):
            due = task.get("due") or "9999-12-31"
            tasks.append({
                "Layer": layer["name"],
                "Task": task["task"],
                "Status": task["status"],
                "Due": due
            })
    return sorted(tasks, key=lambda x: x["Due"])

if __name__ == "__main__":
    rows = all_tasks_sorted()
    print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))
```

### ✅ Run:

```bash
python3 scripts/list_by_due.py
```

---

## ✅ Step 3: Add Local API with FastAPI

### 📦 Install FastAPI and Uvicorn

In your virtualenv:

```bash
pip install fastapi uvicorn
```

### 📄 Create: `signal_noise_toolkit/api.py`

Paste this code into a new file `api.py` inside `signal_noise_toolkit/`:

```python
from fastapi import FastAPI
from pathlib import Path
import yaml

app = FastAPI()
DATA_PATH = Path(__file__).parent / "data" / "layers.yml"

def load_data():
    with open(DATA_PATH, "r") as f:
        return yaml.safe_load(f)["layers"]

@app.get("/tasks")
def get_tasks(layer: str = None, status: str = None):
    results = []
    for entry in load_data():
        if layer and entry["id"] != layer:
            continue
        for task in entry.get("example_tasks", []):
            if status and task["status"] != status:
                continue
            results.append({
                "layer": entry["name"],
                "task": task["task"],
                "created": task["created"],
                "due": task["due"],
                "status": task["status"]
            })
    return results
```

### ✅ Run the API:

```bash
uvicorn api:app --reload
```

Then visit: [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks)
Try adding query filters like `?layer=symbolic&status=done`

---

## 🔜 Next Steps:

1. Want a notebook dashboard?
2. Want pretty HTML output saved to files?
3. Want CLI to write output to disk?

Just say the word. I'll walk you through each, in order.
