# config/db/database_mysql.py
import os, contextlib
from typing import Any, Iterable, List, Mapping, Optional, Sequence, Callable
import mysql.connector as mysql
from mysql.connector import Error
from config.db import config

_SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def get_conn() -> mysql.MySQLConnection:
    """Nueva conexión por llamada (simple y robusta)."""
    return mysql.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB_NAME,
        connection_timeout=8,
        charset="utf8mb4",
        collation="utf8mb4_unicode_ci",
        # auth_plugin="mysql_native_password",
    )

def ensure_schema() -> None:
    """Lee schema.sql, crea la DB si falta y ejecuta los statements.
    Ignora errores de índice duplicado (1061) para evitar fallos si el índice ya existe).
    """
    if not os.path.isfile(_SCHEMA_PATH):
        raise FileNotFoundError(f"schema no encontrado: {_SCHEMA_PATH}")

    # crear DB si falta
    try:
        c = mysql.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASS,
            connection_timeout=8,
            charset="utf8mb4"
        )
        cur = c.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_NAME}")
        cur.close()
        c.close()
    except Error as e:
        raise RuntimeError(f"Error creando DB: {e}")

    # ejecutar schema (solo DDL en schema.sql)
    schema_sql = open(_SCHEMA_PATH, "r", encoding="utf-8").read()
    all_stmts = [s.strip() for s in schema_sql.split(";") if s.strip()]
    # opcional: filtrar solo CREATE/ALTER/DROP (más seguro)
    stmts = [s for s in all_stmts if s.split()[0].upper() in ("CREATE", "ALTER", "DROP")]

    conn = get_conn()
    try:
        cur = conn.cursor()
        for s in stmts:
            try:
                cur.execute(s)
            except Error as e:
                # 1061 = duplicate key name (índice ya existe)
                if getattr(e, "errno", None) in (1061,):
                    continue
                else:
                    raise
        conn.commit()
    finally:
        try: cur.close()
        except: pass
        try: conn.close()
        except: pass

# decorador para garantizar esquema
def _ensure_schema(fn: Callable):
    def wrapper(*args, **kwargs):
        ensure_schema()
        return fn(*args, **kwargs)
    return wrapper

@_ensure_schema
def fetch_all(sql: str, params: Optional[Sequence[Any]] = None, as_dict: bool = True) -> List[Mapping[str, Any]]:
    conn = get_conn()
    try:
        with conn.cursor(dictionary=as_dict) as cur:
            cur.execute(sql, params or ())
            return cur.fetchall() or []
    except Error as e:
        raise RuntimeError(f"[fetch_all] {e}")
    finally:
        try: conn.close()
        except: pass

@_ensure_schema
def fetch_one(sql: str, params: Optional[Sequence[Any]] = None, as_dict: bool = True) -> Optional[Mapping[str, Any]]:
    conn = get_conn()
    try:
        with conn.cursor(dictionary=as_dict) as cur:
            cur.execute(sql, params or ())
            return cur.fetchone()
    except Error as e:
        raise RuntimeError(f"[fetch_one] {e}")
    finally:
        try: conn.close()
        except: pass

@_ensure_schema
def fetch_val(sql: str, params: Optional[Sequence[Any]] = None):
    row = fetch_one(sql, params, as_dict=False)
    if row is None:
        return None
    if isinstance(row, (list, tuple)):
        return row[0]
    return list(row.values())[0]

@_ensure_schema
def execute(sql: str, params: Optional[Sequence[Any]] = None) -> int:
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params or ())
        conn.commit()
        return cur.rowcount
    except Error as e:
        conn.rollback()
        raise RuntimeError(f"[execute] {e}")
    finally:
        try: conn.close()
        except: pass

@_ensure_schema
def executemany(sql: str, seq_of_params: Iterable[Sequence[Any]]) -> int:
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, seq_of_params)
        conn.commit()
        return cur.rowcount
    except Error as e:
        conn.rollback()
        raise RuntimeError(f"[executemany] {e}")
    finally:
        try: conn.close()
        except: pass

@contextlib.contextmanager
def transaction():
    ensure_schema()
    conn = get_conn()
    cur = conn.cursor()
    try:
        yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        try: cur.close()
        except: pass
        try: conn.close()
        except: pass

def health_check() -> bool:
    try:
        ensure_schema()
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            cur.fetchone()
        conn.close()
        return True
    except Exception as e:
        print("health_check error:", e)
        return False
