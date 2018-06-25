import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm

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

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

cursor.execute("SELECT word FROM Analogies_1")
palabras = cursor.fetchall()
cursor.execute("SELECT femenine_word FROM Analogies_1")
femenine_palabras = cursor.fetchall()
cursor.execute("SELECT femenine_value FROM Analogies_1")
femenine = cursor.fetchall()
cursor.execute("SELECT masculine_word FROM Analogies_1")
masculine_palabras = cursor.fetchall()
cursor.execute("SELECT masculine_value FROM Analogies_1")
masculine = cursor.fetchall()
cursor.execute("SELECT tokio_word FROM Analogies_1")
tokio_palabras = cursor.fetchall()
cursor.execute("SELECT tokio_value FROM Analogies_1")
tokio = cursor.fetchall()
cursor.execute("SELECT japan_word FROM Analogies_1")
japan_palabras = cursor.fetchall()
cursor.execute("SELECT japan_value FROM Analogies_1")
japan = cursor.fetchall()
# close the conexion with the data base
conexion.close()

dict = {'Palabras': palabras, '+Women': femenine_palabras, '+Women (valores)': femenine,
        '+Men': masculine_palabras, '+Men (valores)': masculine,
        '+Tokio': tokio_palabras, '+Tokio (valores)': tokio,
        '+Japan': japan_palabras, '+Japan (valores)': japan}

df = pd.DataFrame(dict)

# create a copy of the data in order to use it easily in R
df.to_csv('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/CSV/Analogies_1.csv')
