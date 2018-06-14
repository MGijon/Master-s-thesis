import sqlite3 
import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
	return model.most_similar(positive = ['tokio', word], negative = ['Japan'], topn = Tope)

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
# crete one table for this scipt
cursor.execute('''
	CREATE TABLE Analogies_1 (
			word VARCHAR(20) PRIMARY KEY,
			femenine_word VARCHAR(20),
			femenine_value FLOAT(20), 
			masculine_word VARCHAR(20),
			masculine_value FLOAT(20),
			tokio_word VARCHAR(20),
			tokio_value FLOAT(20),
			japan_word VARCHAR(20),
			japan_value FLOAT(20)
	)''')


## LOOPING:
## =======

words = list(model.wv.vocab)[1:10]
print(add_Japan(words[4])[0])

cursor.execute("INSERT INTO Analogies_1 VALUES ('hola', 'a', 13.31, 'b', 343, 'dwdas', 13.34224, 've', 3233)")
conexion.commit()



# close the conexion with the data base
conexion.close()
