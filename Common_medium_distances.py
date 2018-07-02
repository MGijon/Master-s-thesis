import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import random
import sqlite3

# load the model 1
# ----------------
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model_1 = gm.KeyedVectors.load_word2vec_format(route, binary = True)

# load the model 2
# ----------------
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/freebase-vectors-skipgram1000-en.bin'
model_2 = gm.KeyedVectors.load_word2vec_format(route, binary = True)

vocabulario_1 = list(pickle.load(open("/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Pickle/common_vocabulary.p", "rb" )))

vocabulario_2 = ['/en/' + x for x in vocabulario_1]

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

for i in range(10, 1001):
    auxiliar_1 = model_1.most_similar(vocabulario_1[i], topn = 1)
    auxiliar_2 = model_2.most_similar(vocabulario_2[i], topn = 1)

    resultado = (i, auxiliar_1[0][0], auxiliar_1[0][1], auxiliar_2[0][0], auxiliar_2[0][1])
    Resultado = [resultado]

    print('====\n')
    print(resultado)
    print('====\n')

    try:
        cursor.executemany("INSERT INTO Common VALUES (?, ?, ?, ?, ?)", Resultado)
        conexion.commit()
    except:
        pass


# close the conexion with the data base
conexion.close()
