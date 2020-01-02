import sqlite3

class data:
    def __init__(self):
        self.con=sqlite3.connect("Books.db")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, book VARCHAR(256), author VARCHAR(256), quantity INTEGER, edition INTEGER, link VARCHAR(256))")
        self.con.commit()

    def add(self,book="",author="",quantity="",edition="",link=''):
        self.cur.execute("INSERT INTO students VALUES(NULL,?,?,?,?,?)",(book,author,quantity,edition,link))
        self.con.commit()

    def vall(self):
        self.cur.execute("SELECT * FROM students")
        d=self.cur.fetchall()
        return d

    def reg(self,quantity):
        self.cur.execute("UPDATE  students SET quantity=?",(quantity-1,))
        self.con.commit()

    def acs(self,ID):
        self.cur.execute("SELECT link FROM students WHERE id=?",(ID,))
        d=self.cur.fetchall()
        return d

    def search(self,book="",author="",quantity="",edition=""):
        self.cur.execute("SELECT * FROM students WHERE book=? OR author=? OR quantity=? OR edition=?",(book,author,quantity,edition))
        d=self.cur.fetchall()
        return d

    def delete(self,ID):
        self.cur.execute("DELETE FROM students WHERE id=?",(ID,))
        self.con.commit()

    def update(self,ID,book="",author="",quantity="",edition="",link=''):
        self.cur.execute("UPDATE students SET book=?,author=?,quantity=?,edition=?,link=? WHERE ID=?",(book,author,quantity,edition,link,ID))
        self.con.commit()

    def __del__(self):
        self.con.close()

obj=data()
