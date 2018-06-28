import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import random
import sqlite3

# Cantidad de datos que sumamos a la base de datos
TOPE = 1

# load the model
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

vocabulario = words = list(model.wv.vocab)

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
        # lo clcularemos y ñadiremos, debemos constultar primero al base de datos
        auxiliar = model.distance(vocabulario[aleatorio], vocabulario[aleatorio + 1])
        auxiliar2 = model.most_similar(vocabulario[aleatorio], topn = 1)
        print(vocabulario[aleatorio])
        print("==========")
        print(auxiliar2)



# close the conexion with the data base
conexion.close()
