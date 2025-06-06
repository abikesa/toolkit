# Re-import required libraries due to kernel reset
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph to represent the conditioning analogy
G = nx.DiGraph()

# Add nodes with labels
G.add_node("Stimulus (x1)", layer="input", type="classical")
G.add_node("Response (yi)", layer="output", type="classical")
G.add_node("Propensity Score (x2)", layer="middle", type="classical")

G.add_node("Action (X)", layer="input", type="operant")
G.add_node("Outcome (Y)", layer="output", type="operant")
G.add_node("Confounder (Z)", layer="hidden", type="operant")

# Add edges for classical conditioning analogy
G.add_edge("Stimulus (x1)", "Propensity Score (x2)")
G.add_edge("Propensity Score (x2)", "Response (yi)")

# Add edges for operant conditioning analogy
G.add_edge("Action (X)", "Outcome (Y)")
G.add_edge("Confounder (Z)", "Action (X)")
G.add_edge("Confounder (Z)", "Outcome (Y)")

# Define positions manually for better layout
pos = {
    "Stimulus (x1)": (-2, 1),
    "Propensity Score (x2)": (0, 1),
    "Response (yi)": (2, 1),
    "Confounder (Z)": (0, -0.5),
    "Action (X)": (-1.5, -2),
    "Outcome (Y)": (1.5, -2)
}

# Save the graph as a .jpeg image
output_path = "../learning-epidemiology.jpeg"
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgrey", edge_color="black", font_size=10, font_weight="bold", arrows=True)
plt.title("Classical vs. Operant Conditioning (Propensity Scores vs. Confounding)", fontsize=12)
plt.axis("off")
plt.tight_layout()
plt.savefig(output_path, format="jpeg")
output_path
