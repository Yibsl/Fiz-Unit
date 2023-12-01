import sqlite3 as sq

con = sq.connect("tutorial.db")
cur = con.cursor()

def get(key):
    res = cur.execute(f"SELECT {key} FROM slider_pos")
    print(res.fetchall())

