from flask import Flask, render_template, jsonify, request
import yaml

app = Flask(__name__)

YAML_PATH = "umami.yml"

def load_yaml():
    with open(YAML_PATH, "r") as f:
        return yaml.safe_load(f)

def save_yaml(data):
    with open(YAML_PATH, "w") as f:
        yaml.dump(data, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/layers", methods=["GET", "POST"])
def api_layers():
    if request.method == "POST":
        new_data = request.json
        save_yaml(new_data)
        return jsonify({"status": "saved"})
    return jsonify(load_yaml())

if __name__ == "__main__":
    app.run(debug=True)
