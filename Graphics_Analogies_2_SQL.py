import sqlite3
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

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

route2 = '/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/SQLite/Analogies.db'
conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

def graph_who(rug = False):
	cursor.execute("SELECT who_value FROM Analogies_Questions")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ Who - Thing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Who for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ Who - Thing  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Who for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

def graph_why(rug = False):
	cursor.execute("SELECT why_value FROM Analogies_Questions")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ Why - Thing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Why for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ Why - Thing  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Why for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()


def graph_where(rug = False):
	cursor.execute("SELECT where_value FROM Analogies_Questions")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ Where - Thing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Where for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ Where - Thing  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Where for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()


def graph_when(rug = False):
	cursor.execute("SELECT when_value FROM Analogies_Questions")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ When - Thing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/When for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ When - Thing  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/When for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()


def graph_what(rug = False):
	cursor.execute("SELECT what_value FROM Analogies_Questions")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ What - Thing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/What for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ What - Thing  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/What for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()


def graph_how(rug = False):
	cursor.execute("SELECT how_value FROM Analogies_Questions")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ How - Thing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/How for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ How - Thing  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/How for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()


def graph_whom(rug = False):
	cursor.execute("SELECT whom_value FROM Analogies_Questions")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ Whom - Thing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else: 
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Whom for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ Whom - Thing  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Whom for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()


graph_who()
graph_why()
graph_where()
graph_when()
graph_what()
graph_how()
graph_whom()





'''

def graph_femenine_masculine_1():
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT masculine_value FROM Analogies_1")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Adding masculine and femenine for a total of ' + str(cantidad1) + ' samples.')
	sns.distplot(datos1, label = '+ women')
	sns.distplot(datos2, label = '+ men')
	plt.legend()
	plt.xlabel('WOMEN -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\nMEN -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add femenine and masculine for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

#graph_femenine_masculine_1()

def graph_tokio_japan_1():
	cursor.execute("SELECT tokio_value FROM Analogies_1")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT japan_value FROM Analogies_1")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Adding tokio and japan for a total of ' + str(cantidad1) + ' samples.')
	sns.distplot(datos1, label = '+ tokio')
	sns.distplot(datos2, label = '+ japan')
	plt.legend()
	plt.xlabel('TOKIO -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\nJAPAN -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add tokio and japan for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

graph_tokio_japan_1()
'''
# close the conexion with the data base
conexion.close()
