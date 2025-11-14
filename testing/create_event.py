from config.db.database_mysql import execute
from datetime import datetime, timedelta

user_id = 1
title = "Reunión de prueba"
start_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
end_at = (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
description = "Prueba insert evento desde script."

n = execute(
    "INSERT INTO events (user_id, title, start_at, end_at, description) VALUES (%s,%s,%s,%s,%s)",
    (user_id, title, start_at, end_at, description)
)
print("Filas insertadas:", n)
