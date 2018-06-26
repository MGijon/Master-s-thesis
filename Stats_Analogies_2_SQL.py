import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm

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

def a(lista):
    temporal = []
    for i in lista:
        temporal.append(i[0])
    return temporal

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

cursor.execute("SELECT word FROM Analogies_Questions")
palabras = cursor.fetchall()

cursor.execute("SELECT who_word FROM Analogies_Questions")
who_palabras = cursor.fetchall()
cursor.execute("SELECT who_value FROM Analogies_Questions")
who = cursor.fetchall()

cursor.execute("SELECT why_word FROM Analogies_Questions")
why_palabras = cursor.fetchall()
cursor.execute("SELECT why_value FROM Analogies_Questions")
why = cursor.fetchall()

cursor.execute("SELECT where_word FROM Analogies_Questions")
where_palabras = cursor.fetchall()
cursor.execute("SELECT where_value FROM Analogies_Questions")
where = cursor.fetchall()

cursor.execute("SELECT when_word FROM Analogies_Questions")
when_palabras = cursor.fetchall()
cursor.execute("SELECT when_value FROM Analogies_Questions")
when = cursor.fetchall()

cursor.execute("SELECT what_word FROM Analogies_Questions")
what_palabras = cursor.fetchall()
cursor.execute("SELECT what_value FROM Analogies_Questions")
what = cursor.fetchall()

cursor.execute("SELECT how_word FROM Analogies_Questions")
how_palabras = cursor.fetchall()
cursor.execute("SELECT how_value FROM Analogies_Questions")
how = cursor.fetchall()

cursor.execute("SELECT whom_word FROM Analogies_Questions")
whom_palabras = cursor.fetchall()
cursor.execute("SELECT whom_value FROM Analogies_Questions")
whom = cursor.fetchall()

dict = {'Palabras' : a(palabras),
        'Who_palabras': a(who_palabras), 'Who': a(who),
        'Why_palabras': a(why_palabras), 'Why': a(why),
        'Where_palabras': a(where_palabras), 'Where': a(where),
        'When_palabras': a(when_palabras), 'When': a(when),
        'What_palabras': a(what_palabras), 'What': a(what),
        'How_palabras': a(who_palabras), 'How': a(who),
        'Whom_palabras': a(whom_palabras), 'Whom': a(whom)}

df = pd.DataFrame(dict)

# create a copy of the data in order to use it easily in R
df.to_csv('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/CSV/Analogies_Questions.csv')
