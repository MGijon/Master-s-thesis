import matplotlib.pyplot as plt
import numpy as np

e = np.e
pi = np.pi

def VolumeNSphere(N, R = 1):
    '''Computes the volume of a N Sphere (using Stearling aproximation) in a N dimensionl space as a function od N
    (dimension) and R (radius).'''
    term1 = 1 / (np.sqrt(N * pi))
    term2 = np.power( (2 * pi * e)/N, N/2 )
    expresion = term1 * term2 * np.power(R, N)
    return expresion


x_axis = [x for x in range(1, 50)]
Radious = [(0.9, 'orange'),
           (1, 'red'),
           (1.1, 'purple'),
           #(1.2, 'green'),
           #(1.5,'indigo'),
          # (1.75, 'black')
           ]

def DimensionRadious():
    plt.figure(figsize = (20, 14))
    for Rad in Radious:
        plt.plot(x_axis,
                 [VolumeNSphere(x, R=Rad[0]) for x in x_axis],
                 'ro',
                 linestyle='-',
                 label = 'Radius: ' + str(Rad[0]),
                 c = Rad[1]
                 )

    plt.title('Evolution of the volume of the Sphere as dimension grows for different radious')
    plt.ylabel('Volume')
    plt.xlabel('Dimension')
    plt.legend()
    plt.savefig('VolumeNSphere')
    plt.show()

def Radious1():
    plt.figure(figsize=(20, 14))
    plt.plot(x_axis,
             [VolumeNSphere(N = x, R = 1) for x in x_axis],
             'ro',
             linestyle='-',
             )
    plt.title('Volume of a N-Sphere of radius 1')
    plt.xlabel('Dimension')
    plt.ylabel('Volumen')
    plt.savefig('Volume_N_Sphere_R1')
    plt.show()

DimensionRadious()