from config.db.database_mysql  import DatabaseMysql
db = DatabaseMysql()

import hashlib


class UserModel:

    # ------------------------
    # HASH PASSWORD
    # ------------------------
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    # ------------------------
    # REGISTRO
    # ------------------------
    @staticmethod
    def register(username: str, email: str, password: str) -> bool:

        if not username or not email or not password:
            return False

        if "@" not in email:
            return False

        password_hash = UserModel.hash_password(password)

        sql = """
            INSERT INTO users (username, email, password_hash, role)
            VALUES (%s, %s, %s, %s)
        """

        try:
            db.execute(sql, (username, email, password_hash, "user"))
            return True
        except Exception:
            return False

    # ------------------------
    # LOGIN
    # ------------------------
    @staticmethod
    def login(username: str, password: str):
        if not username or not password:
            return None

        password_hash = UserModel.hash_password(password)

        sql = """
            SELECT id, username, email, role
            FROM users
            WHERE username = %s AND password_hash = %s
        """

        return db.fetch_one(sql, (username, password_hash))

    # ------------------------
    # PRIMER USUARIO
    # ------------------------
    @staticmethod
    def get_first_user():
        sql = "SELECT id, username, email, role FROM users LIMIT 1"
        return db.fetch_one(sql)
