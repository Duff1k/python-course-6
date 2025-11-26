from config import Config
from service.UserService import UserService
from service.ProductService import ProductService
from controller.ProductController import app

class BackendFacade:
    def __init__(self, config: Config | None = None):
        self.config = config or Config()

        self.user_service = UserService()
        self.product_service = ProductService()
        self.user_service.init_schema()
        self.product_service.init_schema()
        self.user_service.ensure_default_users()
        self.app = app

    def run(self, debug: bool = True):
        self.app.run(debug=debug)