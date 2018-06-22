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

Kanemaru_car_value()
