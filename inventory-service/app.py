from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)
inventory = [
    {"id": 1, "item": "Laptop", "stock": 50},
    {"id": 2, "item": "Phone",  "stock": 120},
    {"id": 3, "item": "Tablet", "stock": 30},
]

@app.route('/')
def home():
    return render_template('index.html', inventory=inventory)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/restock', methods=['POST'])
def restock():
    data = request.json
    for item in inventory:
        if item['id'] == data.get('id'):
            item['stock'] += data.get('qty', 10)
    return jsonify({"status": "Restocked"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)