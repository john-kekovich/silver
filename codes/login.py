import sqlite3
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute()))
import const

def check_login(username, password):
    conn = sqlite3.connect(const.DB_PATH)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}';")
    user = cur.fetchall()
    conn.commit()
    conn.close()
    
    if len(user) > 0:
        return True
    else:
        return False