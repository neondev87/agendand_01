# config/db/config.py
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "prueba_db")

# aviso suave si falta algo crítico
_required = ["DB_HOST", "DB_USER", "DB_NAME"]
_missing = [k for k in _required if not globals().get(k)]
if _missing:
    print(f"[config] faltan en .env: {', '.join(_missing)}")
