import sqlite3
import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time

'''
word VARCHAR(20) PRIMARY KEY,

femenine_word VARCHAR(20),
femenine_value FLOAT(20),

masculine_from_femenine_word VARCHAR(20),
masculine_from_femenine_value FLOAT(20),

distance_from_original_word float(20),
'''

## FUNCTIONS:
## ==========

# load the model
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

def add_femenine(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['woman', word], negative = ['man'], topn = Tope)

def add_masculine(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['man', word], negative = ['woman'], topn = Tope)

## SAVING:
## ======
# create the data base
route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

## LOOPING:
## =======

Start = 3000
Stop = 5000

words = list(model.wv.vocab)[Start:Stop]

for i in words:
	femenine = add_femenine(i)[0]
	masculine_femenine = add_masculine(add_femenine(i)[0][0])[0]
	resultado = (i, femenine[0], femenine[1], masculine_femenine[0], masculine_femenine[1], model.distance(femenine[0], masculine_femenine[0]))
	Resultado = [ resultado ]
	cursor.executemany("INSERT INTO Analogies_BF_WM VALUES (?, ?, ?, ?, ?, ?)", Resultado)
	conexion.commit()



# close the conexion with the data base
conexion.close()
