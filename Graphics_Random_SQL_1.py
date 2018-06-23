import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

'''
word VARCHAR(20) PRIMARY KEY,

Kanemaru_car_WORD VARCHAR(20),
Kanemaru_car_value FLOAT(20),

car_Kanemaru_WORD VARCHAR(20),
car_Kanemaru_value FLOAT(20),

Rooftop_Comedy_car_word VARCHAR(20),
Rooftop_Comedy_car_value FLOAT(20),

car_Rooftop_Comedy_word VARCHAR(20),
car_Rooftop_Comedy_value FLOAT(20),

Brahma_Vishnu_car_word VARCHAR(20),
Brahma_Vishnu_car_value FLOAT(20),

car_Brahma_Vishnu_word VARCHAR(20),
car_Brahma_Vishnu_value FLOAT(20)
'''

route2 = '/Users/manuelgijon/Dropbox/TFM/Calculations/Data/Random.db'

conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

def Kanemaru_car_value(rug = False):
	cursor.execute("SELECT Kanemaru_car_value FROM R1")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ Kanemaru - Car for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Kanemaru-car for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ Kanemaru - Car  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Kanemaru-car for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

#Kanemaru_car_value()

def car_Kanemaru_value(rug = False):
	cursor.execute("SELECT car_Kanemaru_value FROM R1")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ Car - Kanemaru for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/car-Kanemaru for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ Car - Kanemaru   for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/car-Kanemaru for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

#car_Kanemaru_value()

def car_and_Kanemaru():
	cursor.execute("SELECT Kanemaru_car_value FROM R1")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT car_Kanemaru_value FROM R1")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Kanemaru and car for a total of ' + str(cantidad1) + ' samples.')
	sns.distplot(datos1, label = '+ Kanemaru - car')
	sns.distplot(datos2, label = '+ car - Kanemaru')
	plt.legend()
	plt.xlabel('+ Kanemaru - car -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\n+ car - Kanemaru -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Kanemau and car for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

car_and_Kanemaru()

def Scatter_car_and_Kanemaru():
	cursor.execute("SELECT Kanemaru_car_value FROM R1")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT car_Kanemaru_value FROM R1")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Scatter Kanemaru and car for a total of ' + str(cantidad1) + ' samples.')
	plt.scatter(datos1, datos2)
	plt.ylabel('+ car - Kanemaru')
	plt.xlabel('+ Kanemaru - car')
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Scatter Kanemau and car for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

Scatter_car_and_Kanemaru()


# close the conexion with the data base
conexion.close()
