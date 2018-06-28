import sqlite3

'''
Create the data base : Distances.db
Create the table.    : Embedding_300
'''

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Distances.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

# crete one table for this scipt
cursor.execute('''
	CREATE TABLE Embedding_300 (
            indice INT PRIMARY KEY,
			word VARCHAR(20),
			nearest_word_distance FLOAT(20)
	)''')

# close the conexion with the data base
conexion.close()
