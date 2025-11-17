import os
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    db_name: str = "users.db"
    host: str = "localhost"
    port: int = 5432  # для PostgreSQL, для SQLite не используется
    
    db_type: str = "sqlite"  # или "postgresql", "mysql"
    

    @classmethod
    def from_env(cls):
        return cls(
            db_name=os.getenv("DB_NAME", "users.db"),
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "5432")),
            db_type=os.getenv("DB_TYPE", "sqlite")
        )

db_config = DatabaseConfig()
