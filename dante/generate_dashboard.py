import yaml
import json
import os
from jinja2 import Environment, FileSystemLoader

# Load YAML data
with open("neurocosmic_layers.yml", "r") as f:
    data = yaml.safe_load(f)
    layers = data["layers"]

# Setup Jinja2 template
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("index_template.html")

# Generate outputs
os.makedirs("output", exist_ok=True)

# HTML
with open("output/index.html", "w") as f:
    f.write(template.render(layers=layers))

# JSON
with open("output/data.json", "w") as f:
    json.dump(layers, f, indent=2)

# Markdown
with open("output/README.md", "w") as f:
    f.write("# Dantean Neurocosmic Framework\n\n")
    f.write("| Icon | Layer | Neurobiology | Dialectic | Axis | Realm |\n")
    f.write("|------|-------|--------------|-----------|------|--------|\n")
    for layer in layers:
        icon = layer.get("icon", "❓")
        name = layer.get("name", "Unnamed")
        neuro = layer.get("neurobiology", "-")
        dialectic = layer.get("dialectic", "-")
        axis = layer.get("axis", "-")
        realm = layer.get("realm", "-")
        f.write(f"| {icon} | {name} | {neuro} | {dialectic} | {axis} | {realm} |\n")

print("✅ Dantean dashboard generated to /output/")

# Save layers to JSON for static fallback use
with open("output/layers.json", "w") as json_out:
    json.dump(layers, json_out, indent=2)
