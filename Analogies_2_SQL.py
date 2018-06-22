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

Start = 2000
Stop = 3000

words = list(model.wv.vocab)[Start:Stop]

for i in words:
	Who = add_who(i)[0]
	Why = add_why(i)[0]
	Where = add_where(i)[0]
	When = add_when(i)[0]
	What = add_what(i)[0]
	How = add_how(i)[0]
	Whom = add_whom(i)[0]
	resultado = (i, Who[0], Who[1], Why[0], Why[1], Where[0], Where[1], When[0], When[1], What[0], What[1], How[0], How[1], Whom[0], Whom[1])
	Resultado = [ resultado ]
	cursor.executemany("INSERT INTO Analogies_Questions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", Resultado)
	conexion.commit()



# close the conexion with the data base
conexion.close()