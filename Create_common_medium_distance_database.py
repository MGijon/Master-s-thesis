import sqlite3

'''
Create the data base : Distances.db
Create the table.    : Common
'''

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Distances.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

# crete one table for this scipt
cursor.execute('''
	CREATE TABLE Common (
            indice INT PRIMARY KEY,
			word_1 VARCHAR(20),
			nearest_word_distance_1 FLOAT(20),
            word_2 VARCHAR(20),
			nearest_word_distance_2 FLOAT(20)
	)''')

# close the conexion with the data base
conexion.close()
