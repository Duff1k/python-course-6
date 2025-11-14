import psycopg2
from db_configuration import db_configuration

class DatabaseConnection:
    def __init__(self):
        self.host = db_configuration["host"]
        self.port = db_configuration["port"]
        self.user = db_configuration["user"]
        self.password = db_configuration["password"]
        self.dbname = db_configuration["dbname"]

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname = self.dbname
        )