from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simulación de datos para ilustrar una API
products = [
    {"id": 1, "name": "Producto A", "price": 100},
    {"id": 2, "name": "Producto B", "price": 150},
    {"id": 3, "name": "Producto C", "price": 200}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/products/random', methods=['GET'])
def get_random_product():
    return jsonify(random.choice(products))

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = {
        "id": len(products) + 1,
        "name": data.get('name'),
        "price": data.get('price')
    }
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
