import sqlite3
import bcrypt
from config import db_config

class UserDatabase:
    def __init__(self):
        self.db_name = db_config.db_name
        self.init_database()
    
    def get_connection(self):
        """Создание подключения к БД"""
        return sqlite3.connect(self.db_name)
    
    def init_database(self):
        """Инициализация таблицы пользователей"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    email TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def hash_password(self, password: str) -> str:
        """Хеширование пароля"""
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return password_hash.decode('utf-8')
    
    def verify_password(self, password: str, password_hash: str) -> bool:
        """Проверка пароля"""
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    
    def create_user(self, username: str, password: str, email: str = None) -> bool:
        """Создание нового пользователя"""
        try:
            password_hash = self.hash_password(password)
            
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (username, password_hash, email)
                    VALUES (?, ?, ?)
                ''', (username, password_hash, email))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            print(f"Пользователь {username} уже существует")
            return False
        except Exception as e:
            print(f"Ошибка при создании пользователя: {e}")
            return False
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """Аутентификация пользователя"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT password_hash FROM users WHERE username = ?
                ''', (username,))
                result = cursor.fetchone()
                
                if result and self.verify_password(password, result[0]):
                    return True
                return False
        except Exception as e:
            print(f"Ошибка при аутентификации: {e}")
            return False
    
    def get_user(self, username: str) -> dict:
        """Получение информации о пользователе"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, username, email, created_at 
                    FROM users WHERE username = ?
                ''', (username,))
                result = cursor.fetchone()
                
                if result:
                    return {
                        'id': result[0],
                        'username': result[1],
                        'email': result[2],
                        'created_at': result[3]
                    }
                return None
        except Exception as e:
            print(f"Ошибка при получении пользователя: {e}")
            return None
    
    def update_password(self, username: str, new_password: str) -> bool:
        """Обновление пароля пользователя"""
        try:
            new_password_hash = self.hash_password(new_password)
            
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users SET password_hash = ? WHERE username = ?
                ''', (new_password_hash, username))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Ошибка при обновлении пароля: {e}")
            return False
    
    def delete_user(self, username: str) -> bool:
        """Удаление пользователя"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM users WHERE username = ?', (username,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Ошибка при удалении пользователя: {e}")
            return False
    
    def get_all_users(self) -> list:
        """Получение списка всех пользователей (без паролей)"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT id, username, email, created_at FROM users
                ''')
                users = []
                for row in cursor.fetchall():
                    users.append({
                        'id': row[0],
                        'username': row[1],
                        'email': row[2],
                        'created_at': row[3]
                    })
                return users
        except Exception as e:
            print(f"Ошибка при получении списка пользователей: {e}")
            return []
