from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, PlainTextResponse
from pathlib import Path
import yaml
from tabulate import tabulate

app = FastAPI()

DATA_PATH = Path(__file__).parent / "data" / "layers.yml"

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

@app.get("/tasks")
def get_tasks(
    layer: str = Query(default=None),
    status: str = Query(default=None),
    format: str = Query(default="json")
):
    layers = load_data()
    tasks = filter_tasks(layers, layer, status)

    if format == "md":
        return PlainTextResponse(tabulate(tasks, headers="keys", tablefmt="github"))
    elif format == "html":
        return HTMLResponse(tabulate(tasks, headers="keys", tablefmt="html"))
    else:
        return tasks

@app.get("/layers")
def get_layers():
    return load_data()
