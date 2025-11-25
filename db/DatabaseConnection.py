import psycopg2
from config import Config

class DatabaseConnection:
    def __init__(self, config: Config = Config()):
        self.config = config

    def get_connection(self):
        return psycopg2.connect(
            host = self.config.DB_HOST,
            port = self.config.DB_PORT,
            database = self.config.DB_NAME,
            user = self.config.DB_USER,
            password = self.config.DB_PASSWORD,
        )