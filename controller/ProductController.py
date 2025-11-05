import flask
from flask import request, jsonify

from service.AuthService import AuthService
from service.ProductService import ProductService

app = flask.Flask(__name__)

product_service = ProductService()
auth_service = AuthService()

def require_auth():
    auth = request.authorization
    if not auth or not auth_service.verify_password(auth.username, auth.password):
        return False
    return True

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(product_service.list_all())

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id: int):
    try:
        return jsonify(product_service.get(product_id))
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route("/products", methods=["POST"])
def create_product():
    if not require_auth():
        return jsonify({"error": "Authorization required"}), 401
    try:
        return jsonify(product_service.create(request.json))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id: int):
    if not require_auth():
        return jsonify({"error": "Authorization required"}), 401
    try:
        return jsonify(product_service.update(product_id, request.json))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id: int):
    if not require_auth():
        return jsonify({"error": "Authorization required"}), 401
    try:
        return jsonify(product_service.delete(product_id))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)


