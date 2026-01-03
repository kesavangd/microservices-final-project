from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to represent a database
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 800}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
