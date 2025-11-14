import psycopg2
from config import Config

class DatabaseConnection:
    def __init__(self):
        self.config = Config()

    def get_connection(self):
        return psycopg2.connect(
            host=self.config.DB_HOST,
            port=self.config.DB_PORT,
            user=self.config.DB_USER,
            password=self.config.DB_PASSWORD,
            dbname=self.config.DB_NAME
        )
