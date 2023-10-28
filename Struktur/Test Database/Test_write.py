import sqlite3 as sq
import time

con = sq.connect("tutorial.db")
cur = con.cursor()

def create():
    cur.execute("CREATE TABLE slider_pos(dpos)")

def add():
    cur.execute("INSERT INTO slider_pos VALUES(45)")
    con.commit()
def delete():
    cur.execute("DROP TABLE slider_pos")
def get(key):
    res = cur.execute(f"SELECT {key} FROM slider_pos")
    print(res.fetchall())

def update_task(con, task):
    """
    update priority, begin_date, and end date of a task
    :param con:
    :param task:
    :return: project id
    """
    sql = f''' UPDATE slider_pos
              SET dpos = {task}'''
    cur = con.cursor()
    cur.execute(sql)
    con.commit()

for x in range(0,100):
    update_task(con,str(x))
    time.sleep(0.3)
    get("dpos")

create()
add()
con.close
get("dpos")