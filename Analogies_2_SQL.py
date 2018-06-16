import sqlite3 
import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
word VARCHAR(20) PRIMARY KEY,

who_word VARCHAR(20),
who_value FLOAT(20), 

why_word VARCHAR(20),
why_value FLOAT(20),
			
where_word VARCHAR(20),
where_value FLOAT(20),
			
when_word VARCHAR(20),
when_value FLOAT(20),
			
what_word VARCHAR(20),
what_value FLOAT(20),
			
how_word VARCHAR(20),
how_value FLOAT(20),
			
whom_word VARCHAR(20),
whom_value FLOAT(20)
'''

## FUNCTIONS:
## ==========

# load the model
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

def add_who(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['who', word], negative = ['thing'], topn = Tope)

def add_why(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['why', word], negative = ['thing'], topn = Tope)

def add_where(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['where', word], negative = ['thing'], topn = Tope)

def add_when(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['when', word], negative = ['thing'], topn = Tope)

def add_what(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['what', word], negative = ['thing'], topn = Tope)

def add_how(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['how', word], negative = ['thing'], topn = Tope)

def add_whom(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['whom', word], negative = ['thing'], topn = Tope)


## SAVING:
## ======
# create the data base
route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

## LOOPING:
## =======

Start = 0
Stop = 1000

words = list(model.wv.vocab)[Start:Stop]

for i in words:
	resultado = (i, add_who(i)[0][0], add_who(i)[0][1], add_why(i)[0][0], add_why(i)[0][1], add_where(i)[0][0], add_where(i)[0][1], add_when(i)[0][0], add_when(i)[0][1], add_what(i)[0][0], add_what(i)[0][1], add_how(i)[0][0], add_how(i)[0][1], add_whom(i)[0][0], add_whom(i)[0][1])
	Resultado = [ resultado ]
	cursor.executemany("INSERT INTO Analogies_Questions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", Resultado)
	conexion.commit()



# close the conexion with the data base
conexion.close()
