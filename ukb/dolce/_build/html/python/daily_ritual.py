import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os

# Ensure output directory exists
os.makedirs("/mnt/data/images", exist_ok=True)

# Define ritual layers with poetic-molecular labels and correct fractal structure
def define_layers():
    return {
        '🌊 Glucocorticoids, Tension': [
            'Shit 💩', 'Saunter 🚶🏾', 'Steam 🌬️', 'Sauna 🔥', 'Spa 🌊', 'Swim 🏊🏾‍♂️'
        ],
        '🚢 Epigenome, Release*': ['Ship 🚢'],
        '🪛🏴‍☠️ Lateral, Suspense': ['Screwdriver 🪛', 'Pirate 🏴‍☠️'],
        '🛟🦈✂️ Pruning, Cantabile': ['Scissors ✂️', 'Shark 🦈', 'Buoy 🛟'],
        '🏝️ Da Capo': ['Seashells 🏝️', 'Rituals', 'Variation', 'Scaling', 'Instinct']
    }

# Assign symbolic colors
def assign_colors():
    color_map = {
        'yellow': ['Ship 🚢'],
        'paleturquoise': ['Shit 💩', 'Pirate 🏴‍☠️', 'Scissors ✂️', 'Seashells 🏝️'],
        'lightgreen': ['Saunter 🚶🏾', 'Buoy 🛟', 'Scaling', 'Variation', 'Rituals'],
        'lightsalmon': ['Steam 🌬️', 'Sauna 🔥', 'Shark 🦈', 'Screwdriver 🪛', 'Instinct'],
        'lightgray': ['Spa 🌊', 'Swim 🏊🏾‍♂️']
    }
    return {node: color for color, nodes in color_map.items() for node in nodes}

# Compute centered x-positions for a layer
def calculate_positions(layer, y_offset):
    x_positions = np.linspace(-((len(layer) - 1) / 2), ((len(layer) - 1) / 2), len(layer))
    return [(x, y_offset) for x in x_positions]

# Create and render the full fractal graph
def visualize_nn():
    layers = define_layers()
    colors = assign_colors()
    G = nx.DiGraph()
    pos = {}
    node_colors = []

    # Add nodes with spatial layout
    for i, (layer_name, nodes) in enumerate(reversed(list(layers.items()))):
        y_offset = i * -2
        positions = calculate_positions(nodes, y_offset)
        for node, position in zip(nodes, positions):
            G.add_node(node, layer=layer_name)
            pos[node] = position
            node_colors.append(colors.get(node, 'lightgray'))

    # Draw edges between sequential layers
    layer_names = list(layers.keys())
    for i in range(len(layer_names) - 1):
        source_layer = layer_names[i]
        target_layer = layer_names[i + 1]
        for source in layers[source_layer]:
            for target in layers[target_layer]:
                G.add_edge(source, target)

    # Draw and save
    plt.figure(figsize=(18, 13))
    nx.draw(
        G, pos, with_labels=True, node_color=node_colors, edge_color='gray',
        node_size=3600, font_size=11, connectionstyle="arc3,rad=0.2"
    )
    plt.title("Ukubona Ritual Fractal: Glucocorticoids → Da Capo", fontsize=22)
    plt.savefig("/mnt/data/images/ukubona-glucocorticoid-fractal.jpeg", dpi=300, bbox_inches='tight')

# Run the visualizer
visualize_nn()