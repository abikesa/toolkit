import yaml
from datetime import datetime

def load_layers():
    with open("umami.yml", "r") as file:
        data = yaml.safe_load(file)
    return data["layers"]

def signal_to_noise_ratio(layer):
    return layer["signal"] / (layer["noise"] + 1e-5)

def print_summary(layers):
    print(f"UMAMI DASHBOARD — {datetime.now().date()}")
    for layer in layers:
        print(f"{layer['symbol']} {layer['name']}: {layer['theme']}")
        print(f"  S/N Ratio: {signal_to_noise_ratio(layer):.2f}")
        print(f"  → {layer['description']}")
        print()

if __name__ == "__main__":
    layers = load_layers()
    print_summary(layers)

