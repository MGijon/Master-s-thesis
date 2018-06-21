import sqlite3
import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def add_Tokio(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['Tokio', word], negative = ['Japan'], topn = Tope)

def add_Japan(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['Japan', word], negative = ['Tokio'], topn = Tope)



## SAVING:
## ======
# create the data base
route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

## LOOPING:
## =======

Start = 28000
Stop = 30000

words = list(model.wv.vocab)[Start:Stop]

for i in words:
	femenine = add_femenine(i)[0]
	masculine = add_masculine(i)[0]
	tokio = add_Tokio(i)[0]
	japan = add_Japan(i)[0]
	resultado = (i, femenine[0], femenine[1], masculine[0], masculine[1], tokio[0], tokio[1], japan[0], japan[1])
	Resultado = [ resultado ]
	try:
		cursor.executemany("INSERT INTO Analogies_1 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", Resultado)
		conexion.commit()
	except:
		pass


# close the conexion with the data base
conexion.close()
