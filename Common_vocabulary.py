import gensim.models as gm
import pandas as pd
import pickle

# load the model 1
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/GoogleNews-vectors-negative300.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

vocabulary_1 = set(list(model.wv.vocab))
print('Model 1: ' + str(len(vocabulary_1)) + ' words in the vocabulary')

print(list(model.wv.vocab)[10])
# load the model 2
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/freebase-vectors-skipgram1000-en.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

vocabulary_2 = set(list(model.wv.vocab))
print('Model 2: ' + str(len(vocabulary_2)) + ' words in the vocabulary')
print(list(model.wv.vocab)[10])

# load the model 3
route = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Models/freebase-vectors-skipgram1000.bin'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

vocabulary_3 = set(list(model.wv.vocab))
print('Model 3: ' + str(len(vocabulary_3)) + ' words in the vocabulary')
print(list(model.wv.vocab)[10])

common_vocabulary_12 = vocabulary_1 & vocabulary_2
print('Common words between models 1 and 2: ' + str(len(common_vocabulary_12)))

common_vocabulary_13 = vocabulary_1 & vocabulary_3
print('Common words between models 1 and 3: ' + str(len(common_vocabulary_13)))

common_vocabulary_23 = vocabulary_2 & vocabulary_3
print('Common words between models 2 and 3: ' + str(len(common_vocabulary_23)))

common_vocabulary = common_vocabulary_12 & vocabulary_3
print('Common words between models 1, 2 and 3: '  + str(len(common_vocabulary)))

pickle.dump(common_vocabulary, open( "/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Pickle/common_vocabulary.p", "wb" ) )

# favorite_color = pickle.load( open( "save.p", "rb" ) )
