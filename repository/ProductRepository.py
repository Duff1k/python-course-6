from psycopg2.extras import RealDictCursor

from db.DatabaseConnection import DatabaseConnection


class ProductRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_all(self):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM products ORDER BY id;")
            return cur.fetchall()

    def get_by_id(self, product_id: int):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
            return cur.fetchone()

    def create(self, name: str, price: float):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("INSERT INTO products (name, price) VALUES (%s, %s) RETURNING *;", (name, price))
            conn.commit()
            return cur.fetchone()

    def update(self, product_id: int, name: str, price: float):
        with self.db.get_connection() as conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("UPDATE products SET name = %s, price = %s WHERE id = %s RETURNING *;", (name, price, product_id))
            conn.commit()
            return cur.fetchone()

    def delete(self, product_id: int):
        with self.db.get_connection() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
            conn.commit()
            return cur.rowcount > 0