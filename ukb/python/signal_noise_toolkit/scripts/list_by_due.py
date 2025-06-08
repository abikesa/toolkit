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
