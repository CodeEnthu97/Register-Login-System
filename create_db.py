import sqlite3

def add():
    con=sqlite3.connect(database=r'ajay.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS register(Id INTEGER PRIMARY KEY AUTOINCREMENT,First_Name text,Last_Name text,Email text,Contact text,Security_q text,Security_Ans text,Password text,Confirm_pass text)")
    con.commit()


add()