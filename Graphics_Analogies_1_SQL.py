import sqlite3
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

'''
word VARCHAR(20) PRIMARY KEY,

femenine_word VARCHAR(20),
femenine_value FLOAT(20), 

masculine_word VARCHAR(20),
masculine_value FLOAT(20),

tokio_word VARCHAR(20),
tokio_value FLOAT(20),

japan_word VARCHAR(20),
japan_value FLOAT(20)
'''

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies_test.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

def graph_femenine_1(rug = False):
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	femeninos = cursor.fetchall()
	cantidad = len(femeninos)
	plt.figure(figsize = (20, 7))
	plt.title('Add femenine for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(femeninos, rug = True)
	else: 
		sns.distplot(femeninos)
	plt.xlabel('Mean : ' + str(np.mean(femeninos)) + ' - STD : ' + str(np.std(femeninos)))
	plt.show()

def graph_masculine_1(rug = False):
	cursor.execute("SELECT masculine_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('Add masculine for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.show()

def graph_femenine_1(rug = False):
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	femeninos = cursor.fetchall()
	cantidad = len(femeninos)
	plt.figure(figsize = (20, 7))
	plt.title('Add femenine for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(femeninos, rug = True)
	else: 
		sns.distplot(femeninos)
	plt.xlabel('Mean : ' + str(np.mean(femeninos)) + ' - STD : ' + str(np.std(femeninos)))
	plt.show()

def graph_femenine_1(rug = False):
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	femeninos = cursor.fetchall()
	cantidad = len(femeninos)
	plt.figure(figsize = (20, 7))
	plt.title('Add femenine for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(femeninos, rug = True)
	else: 
		sns.distplot(femeninos)
	plt.xlabel('Mean : ' + str(np.mean(femeninos)) + ' - STD : ' + str(np.std(femeninos)))
	plt.show()

graph_femenine_1()







# close the conexion with the data base
conexion.close()
