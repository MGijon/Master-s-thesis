import sqlite3

'''
Create the data base : Analogies.db
Create the table.    : Analogies_BF_WM
'''

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies_test.db'
conexion = sqlite3.connect(route2)

# create the cursor pointing to the data base
cursor = conexion.cursor()
# crete one table for this scipt

cursor.execute('''
	CREATE TABLE Analogies_BF_WM (
			word VARCHAR(20) PRIMARY KEY,

			femenine_word VARCHAR(20),
			femenine_value FLOAT(20),

			masculine_from_femenine_word VARCHAR(20),
			masculine_from_femenine_value FLOAT(20),

			distance_from_original_word float(20),
	)''')

# close the conexion with the data base
conexion.close()
