import os

class DatabaseConfig:
    # Базовые настройки по умолчанию
    HOST = os.getenv("DB_HOST", "localhost")
    PORT = int(os.getenv("DB_PORT", 5432))
    USER = os.getenv("DB_USER", "postgres")
    PASSWORD = os.getenv("DB_PASSWORD", "vi888")
    DBNAME = os.getenv("DB_NAME", "products_db")