import flask
from flask import request, jsonify

from service.AuthService import AuthService
from service.ProductService import ProductService

app = flask.Flask(__name__)

# Добавляем CORS headers вручную
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

product_service = ProductService()
auth_service = AuthService()

def require_auth():
    auth = request.authorization
    if not auth or not auth_service.verify_password(auth.username, auth.password):
        return False
    return True

@app.route("/products", methods=["GET", "OPTIONS"])
def get_products():
    if request.method == "OPTIONS":
        return "", 200
    try:
        return jsonify(product_service.list_all())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id: int):
    try:
        return jsonify(product_service.get(product_id))
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route("/products", methods=["POST", "OPTIONS"])
def create_product():
    if request.method == "OPTIONS":
        return "", 200
    if not require_auth():
        return jsonify({"error": "Authorization required"}), 401
    try:
        return jsonify(product_service.create(request.get_json()))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/products/<int:product_id>", methods=["PUT", "OPTIONS"])
def update_product(product_id: int):
    if request.method == "OPTIONS":
        return "", 200
    if not require_auth():
        return jsonify({"error": "Authorization required"}), 401
    try:
        return jsonify(product_service.update(product_id, request.get_json()))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/products/<int:product_id>", methods=["DELETE", "OPTIONS"])
def delete_product(product_id: int):
    if request.method == "OPTIONS":
        return "", 200
    if not require_auth():
        return jsonify({"error": "Authorization required"}), 401
    try:
        product_service.delete(product_id)
        return jsonify({"message": "Product deleted successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


