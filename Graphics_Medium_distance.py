import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

'''
indice INT PRIMARY KEY,
word VARCHAR(20),
nearest_word_distance FLOAT(20)
'''

route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Distances.db'
conexion = sqlite3.connect(route)
# create the cursor pointing to the data base
cursor = conexion.cursor()

## FIGURE 1:
## ========
cursor.execute("SELECT nearest_word_distance FROM Embedding_300")
datos = cursor.fetchall()
cantidad = len(datos)
plt.figure(figsize = (20, 7))
plt.title('Distance to the nearest word for ' + str(cantidad) + ' random samples')
sns.distplot(datos)
plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Distance to the nearest word for ' + str(cantidad) + ' random samples.png')
plt.show()

plt.title('Cumulative: Distance to the nearest word for ' + str(cantidad) + ' random samples.')
sns.distplot(datos,
           hist_kws=dict(cumulative=True),
           kde_kws=dict(cumulative=True))
plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Distance to the nearest word for ' + str(cantidad) + ' random samples._Cumulative.png')
plt.show()
