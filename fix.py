import sqlite3

con = sqlite3.connect("noteDB.db")
c = con.cursor()

# c.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY, note_text TEXT)")
#c.execute("INSERT INTO notes (note_text) VALUES ('hello3')")
#con.commit()

c.execute('de')
con.commit()