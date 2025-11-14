# core/auth.py
from datetime import datetime
from typing import Optional, Dict, Any

import bcrypt

from config.db.database_mysql import fetch_one, execute


def hash_password(plain: str) -> str:
    if plain is None:
        raise ValueError("La contraseña no puede ser None")
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    if not hashed:
        return False
    try:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False


def create_user(username: str, plain_password: str, role: str = "USER") -> int:
    if not username or not plain_password:
        raise ValueError("username y contraseña son requeridos")
    h = hash_password(plain_password)
    n = execute(
        "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
        (username.strip(), h, role),
    )
    return n


def verify_credentials(username: str, plain_password: str) -> Optional[Dict[str, Any]]:
    if not username or plain_password is None:
        return None

    username = username.strip()
    row = fetch_one(
        "SELECT id, username, password_hash, role FROM users WHERE username=%s",
        (username,),
    )
    if not row:
        return None

    stored_hash = row.get("password_hash")
    if not stored_hash:
        return None

    if not verify_password(plain_password, stored_hash):
        return None

    try:
        now = datetime.now()
        execute("UPDATE users SET last_login=%s WHERE id=%s", (now, row["id"]))
    except Exception:
        pass

    return {"id": row["id"], "username": row["username"], "role": row["role"]}


def change_password(user_id: int, new_plain: str) -> bool:
    if not new_plain:
        raise ValueError("La nueva contraseña no puede ser vacía")
    h = hash_password(new_plain)
    n = execute("UPDATE users SET password_hash=%s WHERE id=%s", (h, user_id))
    return bool(n and n > 0)
