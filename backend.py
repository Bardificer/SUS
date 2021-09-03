import json
import sqlite3

database_file='children.db'

def clear_db(): #Creates/Clears database
    con = sqlite3.connect(database_file)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS children (USER,PASS,IP)')
    cur.execute('DELETE FROM children')
    con.commit()
    con.close()

def add_entry(sett):
    con = sqlite3.connect(database_file)
    cur = con.cursor()
    cur.execute('INSERT INTO children VALUES (?,?,?)',tuple(sett))
    con.commit()
    con.close()

def delete_entry(sett):
    con = sqlite3.connect(database_file)
    cur = con.cursor()
    cur.execute('DELETE FROM children WHERE IP = ? AND USER = ?',(sett["ip"],sett["user"]))
    con.commit()
    con.close()

def change_entry(sett):
    delete_entry(sett)
    add_entry(sett)

def allPull():
    con = sqlite3.connect(database_file)
    cur = con.cursor()
    item = list(cur.execute('SELECT * FROM children'))
    con.close()
    return item

def update():
    con = sqlite3.connect(database_file)
    cur = con.cursor()
    if (list(cur.execute("SELECT * FROM targets WHERE IP=? AND USER=?",(sett['ip'],sett['user']))) != []):
        change_entry(sett)
    else:
        add_entry(sett)