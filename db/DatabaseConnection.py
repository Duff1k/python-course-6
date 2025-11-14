import psycopg2
import os
import sys

# Добавляем путь к service в sys.path для корректного импорта
service_path = os.path.join(os.path.dirname(__file__), '..', 'service')
sys.path.insert(0, service_path)

from config import DatabaseConfig

class DatabaseConnection:
    def __init__(self):
        self.config = DatabaseConfig()

    def get_connection(self):
        return psycopg2.connect(
            host=self.config.HOST,
            port=self.config.PORT,
            user=self.config.USER,
            password=self.config.PASSWORD,
            dbname=self.config.DBNAME