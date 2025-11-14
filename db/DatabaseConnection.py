import psycopg2
from config.db_config import DB_CONFIG

class DatabaseConnection:
    def __init__(self):
        self.host = DB_CONFIG["host"]
        self.port = DB_CONFIG["port"]
        self.user = DB_CONFIG["user"]
        self.password = DB_CONFIG["password"]
        self.dbname = DB_CONFIG["dbname"]

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.dbname
        )
