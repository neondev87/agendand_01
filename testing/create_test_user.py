from core.auth import create_user, hash_password
from config.db.database_mysql import fetch_one

username = "admin"
plain = "MiPassDemo123!"
exists = fetch_one("SELECT id FROM users WHERE username=%s", (username,))
if exists:
    print("Usuario ya existe:", username)
else:
    create_user(username, plain, role="ADMIN")
    print("Usuario creado:", username)
