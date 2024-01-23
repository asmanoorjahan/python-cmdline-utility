import sqlite3 as sql


dbCon= sql.connect("filmflixProject/filmflix.db")
dbCursor=dbCon.cursor()