import argparse
import yaml
from datetime import datetime
from pathlib import Path
from tabulate import tabulate

DATA_PATH = Path(__file__).parent / "data" / "layers.yml"

def load_data():
    with open(DATA_PATH, "r") as f:
        return yaml.safe_load(f)

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

def cli():
    parser = argparse.ArgumentParser(description="🎛️ Signal/Noise Task Viewer")
    parser.add_argument("--layer", help="Filter by layer ID")
    parser.add_argument("--status", help="Filter by task status (done/pending)")
    parser.add_argument("--format", choices=["table", "md", "html"], default="table")

    args = parser.parse_args()
    data = load_data()
    layers = data["layers"]


    tasks = filter_tasks(layers, layer=args.layer, status=args.status)

    if args.format == "table":
        print(tabulate(tasks, headers="keys", tablefmt="fancy_grid"))
    elif args.format == "md":
        print(tabulate(tasks, headers="keys", tablefmt="github"))
    elif args.format == "html":
        print(tabulate(tasks, headers="keys", tablefmt="html"))

if __name__ == "__main__":
    cli()
