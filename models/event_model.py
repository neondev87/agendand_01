from config.db import database_mysql as db
from datetime import datetime


class EventModel:

    # ------------------------
    # REGISTRO DE EVENTOS
    # ------------------------
    @staticmethod
    def log(event_type: str, user_id: int = None, details: str = ""):
        """
        Registra un evento simple.
        event_type: 'login_success', 'login_fail', 'register', 'error', etc.
        """

        sql = """
            INSERT INTO events (event_type, user_id, details)
            VALUES (%s, %s, %s)
        """

        try:
            db.execute(sql, (event_type, user_id, details))
            return True
        except:
            return False

    # ------------------------
    # OBTENER TODOS LOS EVENTOS
    # ------------------------
    @staticmethod
    def get_all():
        sql = "SELECT id, event_type, user_id, details, created_at FROM events ORDER BY id DESC"
        return db.fetch_all(sql)

    # ------------------------
    # OBTENER EVENTOS POR USUARIO
    # ------------------------
    @staticmethod
    def get_by_user(user_id: int):
        sql = """
            SELECT id, event_type, details, created_at
            FROM events
            WHERE user_id = %s
            ORDER BY id DESC
        """
        return db.fetch_all(sql, (user_id,))
