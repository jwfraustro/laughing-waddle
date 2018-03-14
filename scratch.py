import sqlite3 as lite
import sys


con = lite.connect('user.db')

cur = con.cursor()

while True:
    name = input("Enter Name: ")
    sql = ("SELECT * FROM Users WHERE Name=?")
    cur.execute(sql, [(name)])
    print(cur.fetchall())