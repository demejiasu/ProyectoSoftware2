from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
import json

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client["product_db"]

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)

app.json_encoder = JSONEncoder

@app.route('/products', methods=['GET'])
def get_products():
    products = list(db.products.find({}))
    for p in products:
        p['_id'] = str(p['_id'])
    return jsonify(products)

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    if not data or not data.get('name'):
        return jsonify({'error': 'Name is required'}), 400
    
    product = {
        'name': data['name'],
        'description': data.get('description', ''),
        'price': data.get('price', 0),
        'stock': data.get('stock', 0),
        'category': data.get('category', 'general'),
        'image': data.get('image', '')
    }
    result = db.products.insert_one(product)
    product['_id'] = str(result.inserted_id)
    return jsonify(product), 201

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    data = request.json
    update_data = {}
    for field in ['name', 'description', 'price', 'stock', 'category', 'image']:
        if field in data:
            update_data[field] = data[field]
    
    if update_data:
        db.products.update_one({'_id': ObjectId(id)}, {'$set': update_data})
    
    product = db.products.find_one({'_id': ObjectId(id)})
    if product:
        product['_id'] = str(product['_id'])
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    result = db.products.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return jsonify({'message': 'Product deleted'})
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)