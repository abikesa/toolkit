import yaml
import json
import os
from jinja2 import Environment, FileSystemLoader

# Paths
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "output"
YAML_FILE = "neurocosmic_layers.yml"

# Load YAML
with open(YAML_FILE, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    layers = data["layers"]

# Setup Jinja
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("index_template.html")

# Render HTML
html_output = template.render(layers=layers)
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_output)

# Save JSON
with open(os.path.join(OUTPUT_DIR, "data.json"), "w", encoding="utf-8") as f:
    json.dump(layers, f, indent=2, ensure_ascii=False)

# Save README
with open(os.path.join(OUTPUT_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write("# Neurocosmic Layer Framework\n\n")
    f.write("| Icon | Layer | Neurobiology | Dialectic | Axis |\n")
    f.write("|------|-------|--------------|-----------|------|\n")
    for l in layers:
        f.write(f"| {l['icon']} | {l['name']} | {l['neurobiology']} | {l['dialectic']} | {l['axis']} |\n")

print("✅ Dashboard generated to /output/")

