from flask import Flask, request, jsonify, send_from_directory
import json, os, time

app = Flask(__name__)
DATA_PATH = os.path.join("dashboard", "data.json")

@app.route('/')
def serve_dashboard():
    return send_from_directory("dashboard", "index.html")

@app.route('/update', methods=['POST'])
def update_data():
    data = request.get_json()
    data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs("dashboard", exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f)
    return jsonify({"status": "success", "data": data})

@app.route('/status')
def status():
    if not os.path.exists(DATA_PATH):
        return jsonify({"status": "no data yet"})
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    print("🚦 Dashboard server running at http://127.0.0.1:5000/")
    app.run(debug=True)
