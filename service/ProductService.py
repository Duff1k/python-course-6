from repository.ProductRepository import ProductRepository

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def list_all(self):
        return self.repo.get_all()

    def get(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        return product

    def create(self, data: dict):
        name = data.get("name")
        price = data.get("price")
        if not name or price is None:
            raise ValueError("Product name or price is required")
        return self.repo.create(name, price)

    def update(self, product_id: int, data: dict):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        name  = data.get("name", product["name"])
        price = data.get("price", product["price"])
        return self.repo.update(product_id, name, price)

    def delete(self, product_id: int):
        deleted = self.repo.delete(product_id)
        if not deleted:
            raise ValueError("Product not found")
        return True



