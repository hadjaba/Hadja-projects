from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

# Load or create the data file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    anime_list = load_data()
    return render_template('index.html', anime_list=anime_list)

@app.route('/add', methods=['POST'])
def add_anime():
    data = load_data()
    new_entry = request.get_json()
    data.append(new_entry)
    save_data(data)
    return jsonify({"message": "Anime added!"})

if __name__ == '__main__':
    app.run(debug=True)