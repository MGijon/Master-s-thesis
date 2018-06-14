import sqlite3 
import gensim.models as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the model
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

def add_femenine(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['woman', 'king'], negative = ['man'], topn = Tope)

def add_masculine(word, Tope = 1):
	'''
	'''
	return model.most_similar(positive = ['man', 'king'], negative = ['woman'], topn = Tope)



# create the data base
conexion = sqlite3.connect('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Relaciones.db')
# create the cursor pointing to the data base
cursor = conexion.cursor()











# close the conexion with the data base
conexion.close()
