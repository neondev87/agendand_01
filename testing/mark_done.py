from config.db.database_mysql import execute
event_id = 1  # id real
user_id = 1
n = execute("UPDATE events SET is_done=1, updated_at=NOW() WHERE id=%s AND user_id=%s", (event_id, user_id))
print("Filas marcadas done:", n)
