from config.db.database_mysql import fetch_one, fetch_all

u = fetch_one("SELECT id, username, last_login FROM users WHERE username=%s", ("admin",))
print("Usuario:", u)

events = fetch_all("SELECT id, title, start_at, end_at, is_done, updated_at FROM events WHERE user_id=%s ORDER BY start_at", (1,))
print("Eventos:", events)
