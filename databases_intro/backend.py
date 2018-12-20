import sqlite3

def connect():
	conn = sqlite3.connect("bookstore.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
	conn.commit()
	conn.close()

def add_entry(title,author,year,isbn):
	conn = sqlite3.connect("bookstore.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
	conn.commit()
	conn.close()

def view_all():
	conn = sqlite3.connect("bookstore.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM books")
	rows=cur.fetchall()
	conn.close()
	return rows

def search_entry(title="",author="",year="",isbn=""):
	conn = sqlite3.connect("bookstore.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM books WHERE title=? or author=? or year=? or isbn=?", (title,author,year,isbn))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect("bookstore.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM books WHERE id=?", (id,))
	conn.commit()
	conn.close()

def update(id,title,author,year,isbn):
	conn = sqlite3.connect("bookstore.db")
	cur = conn.cursor()
	cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
	conn.commit()
	conn.close()

connect()
#add_entry("Deep Work", "Cal Newport", 2010, 9475034)
#print(view_all())