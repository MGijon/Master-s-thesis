import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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

def graph_femenine_1(rug = False):
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('Add femenine for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add femenine for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative: add femenine for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add femenine for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()


def graph_masculine_1(rug = False):
	cursor.execute("SELECT masculine_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('Add masculine for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add masculine for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative: add masculine for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add masculine for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

def graph_tokio_1(rug = False):
	cursor.execute("SELECT tokio_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('Add tokio for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add tokio for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative: add tokio for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add tokio for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

def graph_japan_1(rug = False):
	cursor.execute("SELECT japan_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('Add japan for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add japan for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative: add japan for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add japan for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

#graph_femenine_1()
#graph_masculine_1()
#graph_tokio_1()
#graph_japan_1()

def graph_femenine_masculine_1():
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT masculine_value FROM Analogies_1")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Adding masculine and femenine for a total of ' + str(cantidad1) + ' samples.')
	sns.distplot(datos1, label = '+ women - men')
	sns.distplot(datos2, label = '+ men - women')
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
	sns.distplot(datos1, label = '+ tokio - japan')
	sns.distplot(datos2, label = '+ japan - tokio')
	plt.legend()
	plt.xlabel('TOKIO -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\nJAPAN -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Add Tokio and Japan for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

#graph_tokio_japan_1()

def graph_femenine_masculine_2():
	'''
	Scatter plot
	'''
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT masculine_value FROM Analogies_1")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Masculine and femenine scatter plot for a total of ' + str(cantidad1) + ' samples.')
	plt.scatter(datos1, datos2)
	plt.ylabel('+ men - women')
	plt.xlabel('+ women - men\n\nWOMEN -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\nMEN -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Masculine and femenine scatter plot for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

#graph_femenine_masculine_2()

def graph_tokio_japan_2():
	cursor.execute("SELECT tokio_value FROM Analogies_1")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT japan_value FROM Analogies_1")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Tokio and japan scatter plot for a total of ' + str(cantidad1) + ' samples.')
	plt.scatter(datos1, datos2)
	plt.ylabel('+ japan - tokio')
	plt.xlabel('+ tokio - japan\n\nTOKIO -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\nJAPAN -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Tokio and japan scatter plot for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

#graph_tokio_japan_2()

def media_masculine():
	cursor.execute("SELECT masculine_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)

	paso = 50
	medias = []
	std = []
	for i in range(0, 10):
		medias.append(np.mean(datos[0 : (i + 1)* paso]))
	for i in range(0, 10):
		std.append(np.std(datos[0 : (i + 1)* paso]))
	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the mean and std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias and std men for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.title('Evolution of the mean for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias for men for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Std for men for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

media_masculine()

def media_femenine():
	cursor.execute("SELECT femenine_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)

	paso = 50
	medias = []
	std = []
	for i in range(0, 10):
		medias.append(np.mean(datos[0 : (i + 1)* paso]))
	for i in range(0, 10):
		std.append(np.std(datos[0 : (i + 1)* paso]))
	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the mean and std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias and std for femenine for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.title('Evolution of the mean for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias for femenine for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Std for femenine for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

media_femenine()

def media_tokio():
	cursor.execute("SELECT tokio_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)

	paso = 50
	medias = []
	std = []
	for i in range(0, 10):
		medias.append(np.mean(datos[0 : (i + 1)* paso]))
	for i in range(0, 10):
		std.append(np.std(datos[0 : (i + 1)* paso]))
	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the mean and std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias and std men for Tokio for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.title('Evolution of the mean for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias for men for Tokio for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Std for men for Tokio for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

media_tokio()

def media_japan():
	cursor.execute("SELECT japan_value FROM Analogies_1")
	datos = cursor.fetchall()
	cantidad = len(datos)

	paso = 50
	medias = []
	std = []
	for i in range(0, 10):
		medias.append(np.mean(datos[0 : (i + 1)* paso]))
	for i in range(0, 10):
		std.append(np.std(datos[0 : (i + 1)* paso]))
	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the mean and std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias and std men for Japan for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(medias, color='red', label = 'mean')
	plt.title('Evolution of the mean for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Medias for men for Japan for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.figure(figsize = (20, 7))
	plt.plot(std, color='green', label = 'std')
	plt.title('Evolution of the std for a total of ' + str(cantidad) + ' samples with a step of ' + str(paso))
	plt.legend()
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Std for men for Japan for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

media_japan()

# close the conexion with the data base
conexion.close()
