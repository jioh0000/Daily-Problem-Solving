import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")
cur.execute("INSERT INTO PhoneBook VALUES('Jioh Park', '010-2777-1209');") 
cur.execute("INSERT INTO PhoneBook VALUES('Lim San', '010 9384 3847);")