import gensim.models as gm
import pandas as pd
import pickle

# load the model 1
# ----------------

route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

lista_vocabulario_1 = list(model.wv.vocab)
vocabulary_1 = set(lista_vocabulario_1)
print('Model 1: ' + str(len(vocabulary_1)) + ' words in the vocabulary')

# load the model 2
# ----------------

def limpieza(lista):
    aux = []
    for word in lista:
        word = word.replace('/en/', '')
        aux.append(word)
    return aux


route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/freebase-vectors-skipgram1000-en.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

lista_vocabulario_2 = limpieza(list(model.wv.vocab))
vocabulary_2 = set(lista_vocabulario_2)
print('Model 2: ' + str(len(vocabulary_2)) + ' words in the vocabulary')

# Common words
# ------------

common_vocabulary_12 = vocabulary_1 & vocabulary_2
print('Common words between models 1 and 2: ' + str(len(common_vocabulary_12)))

pickle.dump(common_vocabulary_12, open( "/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Pickle/common_vocabulary.p", "wb" ) )
