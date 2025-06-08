#!/bin/bash

# 👷🏽 Setup folders
mkdir -p signal_noise_toolkit/data
mkdir -p signal_noise_toolkit/scripts
mkdir -p signal_noise_toolkit/notebooks
mkdir -p signal_noise_toolkit/docs

# 📁 Create core YAML file
cat <<EOF > signal_noise_toolkit/data/layers.yml
$(cat <<YAML
$(cat <<'__EOF__'
# Insert the full contents of your current "Signal Noise Toolkit" YAML here.
# Replace this line with that whole block.
__EOF__
) 
YAML
)
EOF

# 🐍 Basic script to parse it
cat <<EOF > signal_noise_toolkit/scripts/load_layers.py
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
EOF

# 📝 Requirements
cat <<EOF > signal_noise_toolkit/requirements.txt
pyyaml
EOF

# ✅ Done
echo "✅ Repo initialized. Next steps:"
echo "1. Run:    cd signal_noise_toolkit"
echo "2. Install deps:  pip install -r requirements.txt"
echo "3. Try it: python scripts/load_layers.py"
