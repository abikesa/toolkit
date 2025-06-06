from flask import Flask, render_template, jsonify, request, Response
import yaml
import json
import os

app = Flask(__name__, template_folder="templates")

# Load YAML once at startup
with open("neurocosmic_layers.yml", "r") as f:
    data = yaml.safe_load(f)
    layers = data["layers"]

@app.route("/")
def index():
    return render_template("index_template.html", layers=layers)

@app.route("/api/layers", methods=["GET"])
def get_layers():
    axis_filter = request.args.get("axis")
    neuro_filter = request.args.get("neurobiology")

    filtered = layers
    if axis_filter:
        filtered = [l for l in filtered if l["axis"].lower() == axis_filter.lower()]
    if neuro_filter:
        filtered = [l for l in filtered if l["neurobiology"].lower() == neuro_filter.lower()]

    return jsonify(filtered)

@app.route("/api/layers/<name>", methods=["GET"])
def get_layer(name):
    for layer in layers:
        if layer["name"].lower() == name.lower():
            return jsonify(layer)
    return jsonify({"error": "Layer not found"}), 404

@app.route("/api/export/json", methods=["GET"])
def export_json():
    response = Response(json.dumps(layers, indent=2), mimetype='application/json')
    response.headers["Content-Disposition"] = "attachment; filename=neurocosmic_layers.json"
    return response

@app.route("/api/export/markdown", methods=["GET"])
def export_markdown():
    md = "# Neurocosmic Layer Framework\n\n"
    md += "| Icon | Layer | Neurobiology | Dialectic | Axis | Realm |\n"
    md += "|------|-------|--------------|-----------|------|--------|\n"
    for layer in layers:
        md += f"| {layer['icon']} | {layer['name']} | {layer['neurobiology']} | {layer['dialectic']} | {layer['axis']} | {layer['realm']} |\n"
    response = Response(md, mimetype='text/markdown')
    response.headers["Content-Disposition"] = "attachment; filename=neurocosmic_layers.md"
    return response

if __name__ == "__main__":
    app.run(debug=True)
