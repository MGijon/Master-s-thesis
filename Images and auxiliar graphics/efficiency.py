import numpy as np
import logging

limit = 100000

# Looger
logger_name = 'efficiency of proposed norm'
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(logger_name + '.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


# Generate random vectors
vector1 = np.random.rand(1, limit)
vector2 = np.random.rand(1, limit)

vector1 = vector1[0]
vector2 = vector2[0]

# Distances
def euclidean(v1 = vector1, v2 = vector2):
	calculo = v1
	for i in range(0, len(v1)):
		calculo[i] = calculo[i] - v2[i]
	suma = 0
	for i in calculo:
		suma += np.power(i, 2)
		value = np.sqrt(suma)
	return value

def proposed(v1 = vector1, v2 = vector2):
	non_sing_changes = 0
	for i in range(0, len(v1)):
		if v1[i] >= 0 and v2[i] >= 0:
			non_sing_changes += 1
		if v1[i] < 0 and v2[i] < 0:
			non_sing_changes += 1
	value = len(v1) - non_sing_changes
	return value


# Computations
logger.info('\n--------------------\n')
logger.info('Starting with Euclidean')
euclidean()
logger.info('Euclidean finished')
logger.info('\n--------------------\n')
logger.info('Starting with Proposed')
proposed()
logger.info('Proposed finished')
logger.info('\n--------------------\n')
