import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import random
import sqlite3
import seaborn as sns

'''
indice INT PRIMARY KEY,
word_1 VARCHAR(20),
nearest_word_distance_1 FLOAT(20),
word_2 VARCHAR(20),
nearest_word_distance_2 FLOAT(20)
'''

# Open the data base
route_data = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Distances.db'
conexion = sqlite3.connect(route_data)
# create the cursor pointing to the data base
cursor = conexion.cursor()


cursor.execute("SELECT nearest_word_distance_1  FROM Common")
distances_1 = cursor.fetchall()

cursor.execute("SELECT nearest_word_distance_2  FROM Common")
distances_2 = cursor.fetchall()

cantidad = len(distances_1)

# Figura 1
# ========

plt.figure(figsize = (20, 7))
sns.distplot(distances_1, label = 'Negative Sampling 300', rug = True)
sns.distplot(distances_2, label = 'Skip Gram 1000', rug = True)
plt.title('Comparation distances for the nearest word for ' + str(cantidad) + ' words')
plt.legend()
plt.xlabel('NS: mean = ' + str(np.mean(distances_1)) + ' std = ' + str(np.std(distances_1)) + ' \nSG: mean = ' + str(np.mean(distances_2)) + ' std = ' + str(np.std(distances_2)))
plt.savefig('Comparation distances for the nearest word for ' + str(cantidad) + ' words.png')
plt.show()

# Figura 2
# ========

plt.figure(figsize = (20, 7))
sns.distplot(distances_1,
         hist_kws=dict(cumulative=True),
         kde_kws=dict(cumulative=True), label = 'Negative Sampling 300')
sns.distplot(distances_2,
         hist_kws=dict(cumulative=True),
         kde_kws=dict(cumulative=True), label = 'Skip Gram 1000')
plt.title('Comparation distances for the nearest word for ' + str(cantidad) + ' words')
plt.legend()
plt.xlabel('NS: mean = ' + str(np.mean(distances_1)) + ' std = ' + str(np.std(distances_1)) + ' \nSG: mean = ' + str(np.mean(distances_2)) + ' std = ' + str(np.std(distances_2)))
plt.savefig('Cumulative .- Comparation distances for the nearest word for ' + str(cantidad) + ' words.png')
plt.show()


# close the conexion with the data base
conexion.close()
