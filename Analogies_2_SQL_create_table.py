import sqlite3 

'''
Create the data base : Analogies.db
Create the table.    : Analogies_Questions
'''

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)

# create the cursor pointing to the data base
cursor = conexion.cursor()
# crete one table for this scipt

cursor.execute('''
	CREATE TABLE Analogies_Questions (
			word VARCHAR(20) PRIMARY KEY,
			who_word VARCHAR(20),
			who_value FLOAT(20), 
			why_word VARCHAR(20),
			why_value FLOAT(20),
			where_word VARCHAR(20),
			where_value FLOAT(20),
			when_word VARCHAR(20),
			when_value FLOAT(20),
			what_word VARCHAR(20),
			what_value FLOAT(20),
			how_word VARCHAR(20),
			how_value FLOAT(20),
			whom_word VARCHAR(20),
			whom_value FLOAT(20)
	)''')

# close the conexion with the data base
conexion.close()
