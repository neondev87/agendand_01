import os
import mysql.connector as mysql
from mysql.connector import Error
from typing import Any, List, Mapping, Optional, Sequence
from config.db import config

_SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


class DatabaseMysql:
    def __init__(self):
        self.conn = None
        self.ensure_schema()

    # ---------------------------
    #   CONEXIÓN
    # ---------------------------
    def connect(self):
        """Crea o devuelve una conexión activa."""
        if self.conn and self.conn.is_connected():
            return self.conn

        self.conn = mysql.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME,
            connection_timeout=8,
            charset="utf8mb4"
        )
        return self.conn

    # ---------------------------
    #   CARGA DE SCHEMA
    # ---------------------------
    def ensure_schema(self):
        """Crea DB y ejecuta schema.sql solo si es necesario."""
        if not os.path.isfile(_SCHEMA_PATH):
            raise FileNotFoundError(f"schema no encontrado: {_SCHEMA_PATH}")

        # Crear DB si falta
        try:
            tmp = mysql.connect(
                host=config.DB_HOST,
                port=config.DB_PORT,
                user=config.DB_USER,
                password=config.DB_PASS
            )
            cur = tmp.cursor()
            cur.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME}")
            cur.close()
            tmp.close()
        except Error as e:
            raise RuntimeError(f"Error creando DB: {e}")

        # Ejecutar schema
        schema_sql = open(_SCHEMA_PATH, "r", encoding="utf-8").read()
        statements = [s.strip() for s in schema_sql.split(";") if s.strip()]

        conn = self.connect()
        cur = conn.cursor()

        for s in statements:
            try:
                cur.execute(s)
            except Error as e:
                # Ignorar índice duplicado
                if getattr(e, "errno", None) == 1061:
                    continue
                else:
                    raise

        conn.commit()
        cur.close()

    # ---------------------------
    #   CONSULTAS GENÉRICAS
    # ---------------------------
    def fetch_all(self, sql: str, params: Optional[Sequence[Any]] = None):
        conn = self.connect()
        try:
            with conn.cursor(dictionary=True) as cur:
                cur.execute(sql, params or ())
                return cur.fetchall() or []
        except Error as e:
            raise RuntimeError(f"[fetch_all] {e}")

    def fetch_one(self, sql: str, params: Optional[Sequence[Any]] = None):
        conn = self.connect()
        try:
            with conn.cursor(dictionary=True) as cur:
                cur.execute(sql, params or ())
                return cur.fetchone()
        except Error as e:
            raise RuntimeError(f"[fetch_one] {e}")

    def execute(self, sql: str, params: Optional[Sequence[Any]] = None):
        conn = self.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params or ())
            conn.commit()
            return True
        except Error as e:
            conn.rollback()
            raise RuntimeError(f"[execute] {e}")

    # ---------------------------
    #   MÉTODOS DE TU AGENDA
    # ---------------------------
    def get_user(self):
        row = self.fetch_one("SELECT nombre FROM usuarios LIMIT 1")
        return row["nombre"] if row else "Sin usuario"

    def get_events(self):
        return self.fetch_all("SELECT * FROM eventos ORDER BY fecha ASC")

