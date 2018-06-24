import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

'''
word VARCHAR(20) PRIMARY KEY,

nab_sexual_predators_abductor_muscle_WORD VARCHAR(20),
nab_sexual_predators_abductor_muscle_VALUE FLOAT(20),

abductor_muscle_nab_sexual_predators_WORD VARCHAR(20),
abductor_muscle_nab_sexual_predators_VALUE FLOAT(20),

Naked_Juice_molecule_sequencing_WORD VARCHAR(20),
Naked_Juice_molecule_sequencing_VALUE FLOAT(20),

molecule_sequencing_Naked_Juice_WORD VARCHAR(20),
molecule_sequencing_Naked_Juice_VALUE FLOAT(20),

IMPOTENCE_VIAGRA_halloween_costume_WORD VARCHAR(20),
IMPOTENCE_VIAGRA_halloween_costume_VALUE FLOAT(20),

halloween_costume_IMPOTENCE_VIAGRA_WORD VARCHAR(20),
halloween_costume_IMPOTENCE_VIAGRA_VALUE FLOAT(20)
'''

route2 = '/Users/manuelgijon/Dropbox/TFM/Calculations/Data/Random.db'

conexion = sqlite3.connect(route2)
# create the cursor pointing to the data base
cursor = conexion.cursor()

def GRAPHIC_1(rug = False):
	'''
	nab_sexual_predators_abductor_muscle_VALUE
	'''
	cursor.execute("SELECT nab_sexual_predators_abductor_muscle_VALUE FROM R2")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ nab_sexual_predators - abductor_muscle for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/nab_sexual_predators-abductor_muscle for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative:+ nab_sexual_predators - abductor_muscle  for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/nab_sexual_predators-abductor_muscle  for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

	'''
	abductor_muscle_nab_sexual_predators_VALUE
	'''
	cursor.execute("SELECT abductor_muscle_nab_sexual_predators_VALUE FROM R2")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ abductor_muscle - nab_sexual_predators for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/abductor_muscle-nab_sexual_predators for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative: + abductor_muscle - nab_sexual_predators for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/abductor_muscle-nab_sexual_predators for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

	'''
	nab_sexual_predators_abductor_muscle_VALUE & abductor_muscle_nab_sexual_predators_VALUE
	'''
	cursor.execute("SELECT nab_sexual_predators_abductor_muscle_VALUE FROM R2")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT abductor_muscle_nab_sexual_predators_VALUE FROM R2")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('nab_sexual_predators and abductor_muscle for a total of ' + str(cantidad1) + ' samples.')
	sns.distplot(datos1, label = '+ nab_sexual_predators - abductor_muscle')
	sns.distplot(datos2, label = '+ abductor_muscle - nab_sexual_predators')
	plt.legend()
	plt.xlabel('+ nab_sexual_predators - abductor_muscle -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\n+ abductor_muscle - nab_sexual_predators -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/nab_sexual_predators and abductor_muscle for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

	'''
	Scatter nab_sexual_predators_abductor_muscle_VALUE & abductor_muscle_nab_sexual_predators_VALUE
	'''
	cursor.execute("SELECT nab_sexual_predators_abductor_muscle_VALUE FROM R2")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT abductor_muscle_nab_sexual_predators_VALUE FROM R2")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Scatter nab_sexual_predators and abductor_muscle for a total of ' + str(cantidad1) + ' samples.')
	plt.scatter(datos1, datos2)
	plt.ylabel('+ nab_sexual_predators - abductor_muscle')
	plt.xlabel('+ abductor_muscle - nab_sexual_predators')
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Scatter nab_sexual_predators and abductor_muscle for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

#GRAPHIC_1()

def GRAPHIC_2(rug = False):
	'''
	Naked_Juice_molecule_sequencing_VALUE
	'''
	cursor.execute("SELECT Naked_Juice_molecule_sequencing_VALUE FROM R2")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ Naked_Juice - molecule_sequencing for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Naked_Juice-molecule_sequencing for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative: + Naked_Juice - molecule_sequencing for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Naked_Juice-molecule_sequencing for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

	'''
	molecule_sequencing_Naked_Juice_VALUE
	'''
	cursor.execute("SELECT molecule_sequencing_Naked_Juice_VALUE FROM R2")
	datos = cursor.fetchall()
	cantidad = len(datos)
	plt.figure(figsize = (20, 7))
	plt.title('+ molecule_sequencing - Naked_Juice for a total of ' + str(cantidad) + ' samples.')
	if rug:
		sns.distplot(datos, rug = True)
	else:
		sns.distplot(datos)
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/molecule_sequencing-Naked_Juice for a total of ' + str(cantidad) + ' samples.png')
	plt.show()

	plt.title('Cumulative: + molecule_sequencing - Naked_Juice for a total of ' + str(cantidad) + ' samples.')
	sns.distplot(datos,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
	plt.xlabel('Mean : ' + str(np.mean(datos)) + ' - STD : ' + str(np.std(datos)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/molecule_sequencing-Naked_Juice for a total of ' + str(cantidad) + ' samples_Cumulative.png')
	plt.show()

	'''
	Naked_Juice_molecule_sequencing_VALUE & molecule_sequencing_Naked_Juice_VALUE
	'''
	cursor.execute("SELECT Naked_Juice_molecule_sequencing_VALUE FROM R2")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT molecule_sequencing_Naked_Juice_VALUE FROM R2")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Naked_Juice and molecule_sequencing for a total of ' + str(cantidad1) + ' samples.')
	sns.distplot(datos1, label = '+ Naked_Juice - molecule_sequencing')
	sns.distplot(datos2, label = '+ molecule_sequencing - Naked_Juice')
	plt.legend()
	plt.xlabel('+ Naked_Juice - molecule_sequencing -> Mean : ' + str(np.mean(datos1)) + ' - STD : ' + str(np.std(datos1)) + '\n+ molecule_sequencing - Naked_Juice -> Mean : ' + str(np.mean(datos2)) + ' - STD : ' + str(np.std(datos2)))
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Naked_Juice and molecule_sequencing for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

	'''
	Scatter Naked_Juice_molecule_sequencing_VALUE & molecule_sequencing_Naked_Juice_VALUE
	'''
	cursor.execute("SELECT Naked_Juice_molecule_sequencing_VALUE FROM R2")
	datos1 = cursor.fetchall()
	cantidad1 = len(datos1)
	cursor.execute("SELECT molecule_sequencing_Naked_Juice_VALUE FROM R2")
	datos2 = cursor.fetchall()
	cantidad2 = len(datos2)
	plt.figure(figsize = (20, 7))
	plt.title('Scatter Naked_Juice and molecule_sequencing for a total of ' + str(cantidad1) + ' samples.')
	plt.scatter(datos1, datos2)
	plt.ylabel('+ Naked_Juice - molecule_sequencing')
	plt.xlabel('+ molecule_sequencing - Naked_Juice')
	plt.savefig('/Users/manuelgijon/Documents/Programación/Masters_thesis/Data/Images/Scatter Naked_Juice and molecule_sequencing for a total of ' + str(cantidad1) + ' samples.png')
	plt.show()

#GRAPHIC_2()


# close the conexion with the data base
conexion.close()
