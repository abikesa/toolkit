# export_views.py

from pathlib import Path
import yaml
from tabulate import tabulate

DATA_PATH = Path(__file__).parent / "data" / "layers.yml"
DOCS_PATH = Path(__file__).parent / "docs"
DOCS_PATH.mkdir(exist_ok=True)

def load_data():
    with open(DATA_PATH, "r") as f:
        return yaml.safe_load(f)["layers"]

def filter_tasks(layers, layer=None, status=None):
    results = []
    for entry in layers:
        if layer and entry["id"] != layer:
            continue
        for task in entry.get("example_tasks", []):
            if status and task["status"] != status:
                continue
            results.append({
                "Layer": entry["name"],
                "Task": task["task"],
                "Created": task["created"],
                "Due": task["due"] or "TBD",
                "Status": task["status"]
            })
    return results

def export_all():
    layers = load_data()
    statuses = ["done", "pending"]

    for layer in layers:
        layer_id = layer["id"]
        for status in statuses:
            tasks = filter_tasks(layers, layer=layer_id, status=status)

            if tasks:
                filename_md = f"{layer_id}_{status}.md"
                filename_html = f"{layer_id}_{status}.html"

                with open(DOCS_PATH / filename_md, "w") as f_md:
                    f_md.write(tabulate(tasks, headers="keys", tablefmt="github"))

                with open(DOCS_PATH / filename_html, "w") as f_html:
                    f_html.write(tabulate(tasks, headers="keys", tablefmt="html"))

if __name__ == "__main__":
    export_all()
