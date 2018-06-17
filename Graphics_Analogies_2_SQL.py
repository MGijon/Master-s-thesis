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


#graph_who()
#graph_why()
#graph_where()
#graph_when()
#graph_what()
#graph_how()
#graph_whom()

def together():
	cursor.execute("SELECT who_value FROM Analogies_Questions")
	datos1 = cursor.fetchall()
	cantidad = len(datos1)

	cursor.execute("SELECT why_value FROM Analogies_Questions")
	datos2 = cursor.fetchall()

	cursor.execute("SELECT where_value FROM Analogies_Questions")
	datos3 = cursor.fetchall()

	cursor.execute("SELECT when_value FROM Analogies_Questions")
	datos4 = cursor.fetchall()

	cursor.execute("SELECT what_value FROM Analogies_Questions")
	datos5 = cursor.fetchall()

	cursor.execute("SELECT how_value FROM Analogies_Questions")
	datos6 = cursor.fetchall()

	cursor.execute("SELECT whom_value FROM Analogies_Questions")
	datos7 = cursor.fetchall()

	plt.figure(figsize = (20, 7))
	plt.title('For a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos1, label = '+ who - thing')
	sns.distplot(datos2, label = '+ why - thing')
	sns.distplot(datos3, label = '+ where - thing')
	sns.distplot(datos4, label = '+ when - thing')
	sns.distplot(datos5, label = '+ what - thing')
	sns.distplot(datos6, label = '+ how - thing')
	sns.distplot(datos7, label = '+ whom - thing')
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Interrogative - thing for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

together()
