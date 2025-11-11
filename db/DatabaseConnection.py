import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

class DatabaseConnection:
    def __init__(self):
        load_dotenv()  # Загружаем переменные из .env

        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.dbname = os.getenv("DB_NAME")

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.dbname
        )
