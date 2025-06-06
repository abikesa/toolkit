import yaml
from pathlib import Path

def load_layers():
    with open(Path(__file__).parent.parent / 'data' / 'layers.yml', 'r') as f:
        data = yaml.safe_load(f)
    for layer in data['layers']:
        print(f"[{layer['name']}] → {layer['metaphor']}")
        print(f"  Timeline: {layer['business_timeline']}")
        print(f"  Signal Ratio: {layer['ratio']}")
        print(f"  Example task(s):")
        for task in layer.get('example_tasks', []):
            print(f"   - {task['task']} (Created: {task['created']})")
        print()

if __name__ == "__main__":
    load_layers()
