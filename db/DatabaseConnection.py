import psycopg2
from db.config import db_host, db_port, db_name, db_user, db_password

class DatabaseConnection:
    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.user = "postgres"
        self.password = "postgres"
        self.dbname = "products_db"
        self.host = db_host
        self.port = db_port
        self.user = db_user
        self.password = db_password
        self.dbname = db_name

    def get_connection(self):
        return psycopg2.connect(
@@ -15,4 +16,4 @@ def get_connection(self):
            user=self.user,
            password=self.password,
            dbname = self.dbname
        )
        )
