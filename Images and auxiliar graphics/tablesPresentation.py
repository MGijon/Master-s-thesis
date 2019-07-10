import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

## ============================================================== ##
## [(distance, value all vocabulary, value just words in WordNet] ##
## ============================================================== ##

# data dimension 300 GloVe
# ------------------------

G300Synonyms = [('Euclidean', 0.2037, 0.4469),
		('Cosine', 0.2623, 0.5368),
		('Correlation', 0.2629, 0.5358),
		('Canberra', 0.4692, 0.4993),
		('Braycurtis', 0.4270, 0.5359),
		('Proposed', 0.4619, 0.4883),]
G300Antonyms = [('Euclidean', 0.2692, 0.5286), 
                ('Cosine', 0.3745, 0.6352), 
                ('Correlation', 0.3759, 0.6347), 
                ('Canberra', 0.5801, 0.5954), 
                ('Braycurtis', 0.5496, 0.6435), 
                ('Proposed', 0.5794, 0.5998),]
G300SynonymsAntonyms = [('Euclidean', ), 
                	('Cosine', ), 
               	 	('Correlation', ), 
                	('Canberra', ), 
                	('Braycurtis', ), 
                	('Proposed', ),]

# data dimension 300 Word2Vec
# ---------------------------

W300Synonyms = [('Euclidean', 0.2926, 0.4153), 
                ('Cosine', 0.7224, 0.6502), 
                ('Correlation', 0.7234, 0.6509), 
                ('Canberra', 0.6287, 0.6170), 
                ('Braycurtis', 0.7073, 0.6575), 
                ('Proposed', 0.6564, 0.6026),]
W300Antonyms = [('Euclidean', 0.3387, 0.4677), 
                ('Cosine', 0.7939, 0.7035), 
                ('Correlation', 0.7695, 0.7035), 
                ('Canberra', 0.7074, 0.6667), 
                ('Braycurtis', 0.7580, 0.7075), 
                ('Proposed', 0.7140, 0.6505),]
W300SynonymsAntonyms = [('Euclidean', ),
                        ('Cosine', ),
                        ('Correlation', ),
                        ('Canberra', ),
                        ('Braycurtis', ),
                        ('Proposed', ),]

## ======== ##
## Graphics ##
## ======== ##

# GloVe 300
# ---------

fig, ax = plt.subplots(1, 2)
plt.gcf().subplots_adjust(bottom=0.30)

norms = [x[0] for x in G300Synonyms]
G300SynonymsAll = [x[1] for x in G300Synonyms]
G300SynonymsWN = [x[2] for x in G300Synonyms]

G300SAll = pd.Series(G300SynonymsAll, index = norms)
G300SWN = pd.Series(G300SynonymsWN, index = norms)

G300SAll.plot("bar", ax=ax[0], alpha=.45, ylim=[0, 0.65]).set_title("All vocabulary")
G300SWN.plot("bar", ax=ax[1], alpha=.45, ylim=[0, 0.65]).set_title("WordNet vocabulary")

plt.savefig("GloVe300Synonyms")
plt.show()

# Word2Vec 300
# ------------

fig, ax = plt.subplots(1, 2)
plt.gcf().subplots_adjust(bottom=0.30)

norms = [x[0] for x in W300Synonyms]
W300SynonymsAll = [x[1] for x in W300Synonyms]
W300SynonymsWN = [x[2] for x in W300Synonyms]

W300SAll = pd.Series(W300SynonymsAll, index = norms)
W300SWN = pd.Series(W300SynonymsWN, index = norms)

W300SAll.plot("bar", ax=ax[0], alpha=.45, ylim=[0, 1]).set_title("All vocabulary")
W300SWN.plot("bar", ax=ax[1], alpha=.45, ylim=[0, 1]).set_title("WordNet vocabulary")

plt.savefig("Word2Vec300Synonyms")
plt.show()
