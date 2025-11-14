import hashlib
import secrets

def hash_password(password: str) -> tuple[str, str]:
    salt = secrets.token_hex(16)
    salted_password = password + salt
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password, salt

def verify_password(password: str, hashed_password: str, salt: str) -> bool:
    salted_password = password + salt
    return hashlib.sha256(salted_password.encode()).hexdigest() == hashed_password