# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:24:35 2019

@author: Hp
"""
import sqlite3
class Records:
    def __init__(self):
        self.con=sqlite3.connect("studentRecord.db")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students(name VARCHAR,password VARCHAR, book VARCHAR, author VARCHAR, edition VARCHAR, date VARCHAR)")
        self.con.commit()
    def register(self,name,passwd,book,author,edition,date):
        self.cur.execute("INSERT INTO students VALUES(?,?,?,?,?,?)",(name,passwd,book,author,edition,date))
        self.con.commit()
    def vall(self):
        data=self.cur.execute("SELECT * FROM students").fetchall()
        return data
    def search(self,name="",passwd="",book="",author="",edition="",date=""):
        self.cur.execute("SELECT * FROM students WHERE name=? OR password=? OR book=? OR author=? OR edition=? OR date=?",(name,passwd,book,author,edition,date))
        d=self.cur.fetchall()
        return d
    def delete(self,ID):
        self.cur.execute("DELETE FROM students WHERE name=?",(ID,))
        self.con.commit()
    def __del__(self):
        self.con.close()
        
