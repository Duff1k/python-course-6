import psycopg2
import yaml

class DatabaseConnection:
    def __init__(self):
        with open('../configDB.yml', 'r') as f:
            data = yaml.full_load(f)
        self.host = data['db_conf']['host']
        self.port = data['db_conf']['port']
        self.user = data['db_conf']['user']
        self.password = data['db_conf']['password']
        self.dbname = data['db_conf']['dbname']

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname = self.dbname
        )