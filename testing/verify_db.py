# verify_db.py
from config.db import ensure_schema, health_check

print("Verificando esquema y conexión...")
try:
    ensure_schema()
    ok = health_check()
    print("DB OK ✅" if ok else "DB ❌")
    if ok:
        tables = fetch_all("SHOW TABLES", as_dict=False)
        print("Tablas encontradas:", [t[0] for t in tables])
except Exception as e:
    print("Error verificando DB:", e)
