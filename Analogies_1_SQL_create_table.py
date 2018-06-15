import sqlite3 

'''
Create the data base : Analogies.db
Create the table.    : Analogies_1
'''

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)

# create the cursor pointing to the data base
cursor = conexion.cursor()
# crete one table for this scipt

cursor.execute('''
	CREATE TABLE Analogies_1 (
			word VARCHAR(20) PRIMARY KEY,
			femenine_word VARCHAR(20),
			femenine_value FLOAT(20), 
			masculine_word VARCHAR(20),
			masculine_value FLOAT(20),
			tokio_word VARCHAR(20),
			tokio_value FLOAT(20),
			japan_word VARCHAR(20),
			japan_value FLOAT(20)
	)''')

# close the conexion with the data base
conexion.close()
