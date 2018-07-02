import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import random
import sqlite3

# Cantidad de datos que sumamos a la base de datos
TOPE = 30000

# load the model
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

vocabulario = list(model.wv.vocab)

'''
indice INT PRIMARY KEY,
word VARCHAR(20),
nearest_word_distance FLOAT(20)
'''

# Open the data base
route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Distances.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

cursor.execute("SELECT indice FROM Embedding_300")
indexes = cursor.fetchall()

for i in range(0, TOPE):
    aleatorio = random.randint(0, len(vocabulario))
    if aleatorio not in indexes:
        auxiliar = model.most_similar(vocabulario[aleatorio], topn = 1)
        print(vocabulario[aleatorio])
        print("==========")
        print(auxiliar[0][0])
        print(auxiliar[0][1])
        resultado = (aleatorio, auxiliar[0][0], auxiliar[0][1])
        Resultado = [resultado]
        try:
            cursor.executemany("INSERT INTO Embedding_300 VALUES (?, ?, ?)", Resultado)
            conexion.commit()
        except:
            pass


# close the conexion with the data base
conexion.close()
