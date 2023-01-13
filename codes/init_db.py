import sqlite3
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute()))
import const

conn = sqlite3.connect(const.DB_PATH)
cur = conn.cursor()
# cur.execute("DROP TABLE users")
cur.execute("""CREATE TABLE if not exists users(
            id integer PRIMARY KEY AUTOINCREMENT,
            username varchar(20) NOT NULL UNIQUE,
            password varchar(20) NOT NULL
            )""")

conn.commit()
conn.close()
