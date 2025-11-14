from config.db.database_mysql import execute
from datetime import datetime

event_id = 1   # cambia por el id real
user_id = 1
new_title = "Reunión actualizada"
new_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_end = None
new_description = "Cambié la descripción."

n = execute(
    "UPDATE events SET title=%s, start_at=%s, end_at=%s, description=%s WHERE id=%s AND user_id=%s",
    (new_title, new_start, new_end, new_description, event_id, user_id)
)
print("Filas actualizadas:", n)
