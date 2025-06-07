from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import yaml
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data.yml'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return yaml.safe_load(f) or {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        yaml.dump(data, f)

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(load_data())

@app.route('/update', methods=['POST'])
def update_data():
    new_data = request.get_json()
    save_data(new_data)
    return jsonify({"message": "Data updated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/owners')
def get_owners():
    data = load_data()
    owners = set()
    for layer in data.get("layers", {}).values():
        for task in layer.get("tasks", []):
            owners.add(task.get("owner", "unknown"))
    return jsonify(sorted(owners))

@app.route('/api/tasks/<owner>')
def get_tasks_by_owner(owner):
    data = load_data()
    filtered_tasks = []
    for layer_key, layer in data.get("layers", {}).items():
        for task in layer.get("tasks", []):
            if task.get("owner") == owner:
                task_info = task.copy()
                task_info["layer"] = layer.get("name", layer_key)
                task_info["layerColor"] = layer.get("color", "#cccccc")
                filtered_tasks.append(task_info)
    return jsonify(filtered_tasks)
