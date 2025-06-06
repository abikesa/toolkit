# physiology.py — Logic Layer (Flask API)
from flask import Flask, jsonify, request, render_template
import yaml
import datetime

app = Flask(__name__)

with open('anatomy.yml', 'r') as f:
    anatomy = yaml.safe_load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tasks')
def get_tasks():
    return jsonify(anatomy.get("tasks", []))

@app.route('/api/roles')
def get_roles():
    return jsonify(anatomy.get("roles", []))

@app.route('/api/layers')
def get_layers():
    return jsonify(anatomy.get("layers", []))

@app.route('/api/status')
def status():
    today = datetime.date.today().isoformat()
    return jsonify({"status": "alive", "date": today})

if __name__ == '__main__':
    app.run(debug=True)

