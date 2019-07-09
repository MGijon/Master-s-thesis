import matplotlib.pyplot as plt
import seaborn as sns


# data -> distance [dimension 50, dimension 100, dimension 200, dimension 300]
# ====

euclidean_all = [0.4193, 0.5296, 0.4221, 0.2073]
euclidean_WN = [0.4430, 0.3318, 0.3737, 0.4469]
euclidean = [euclidean_all,
             euclidean_WN,
             'euclideanDimensionalComparation',
             'Euclidean Distance',
             'Euclidean',
             'orange'
             ]

cosine_all = [0.2630, 0.2876, 0.3019, 0.2629]
cosine_WN = [0.5160, 0.5365, 0.5486, 0.5368]
cosine = [cosine_all,
          cosine_WN,
          'cosineDimensionalComparation',
          'Cosine distance',
          'Cosine',
          'red'
          ]

correlation_all = [0.2566, 0.2841, 0.3026, 0.2629]
correlation_WN = [0.5123, 0.5349, 0.5470, 0.5358]
correlation = [correlation_all,
               correlation_WN,
               'correlationDimensionalComparation',
               'Correlation distance',
               'Correlation',
               'purple'
               ]

canberra_all = [0.3989, 0.3603, 0.4374, 0.4692]
canberra_WN = [0.4476, 0.4741, 0.5076, 0.4993]
canberra = [canberra_all,
            canberra_WN,
            'canberraDimensionalComparation',
            'Canberra distance',
            'Canberra',
            'green'
            ]

braycurtis_all = [0.3808, 0.3552, 0.4216, 0.4270]
braycurtis_WN = [0.5082, 0.5286, 0.5471, 0.5359]
braycurtis = [braycurtis_all,
              braycurtis_WN,
              'braycurtisDimensionalComparation',
              'Braycurtis distance',
              'Braycurtis',
              'indigo'
              ]

proposed_all = [0.4037, 0.3709, 0.4371, 0.4619]
proposed_WN = [0.4254, 0.4711, 0.4951, 0.4883]
proposed = [proposed_all,
            proposed_WN,
            'proposedDimensionalComparation',
            'Proposed distance',
            'Proposed',
            'black'
            ]

x_axis = [50, 100, 200, 300] # dimensions

data = [euclidean, cosine, correlation, canberra, braycurtis, proposed]

# images
# ======

def firstOnes():
    for distance in data:
        plt.figure(figsize = (20, 14))
        plt.plot(x_axis, distance[0], 'ro', linestyle='-', label='all vocabulary')
        plt.plot(x_axis, distance[1], 'bo', linestyle='-', label='just WN words')
        plt.ylabel('Kolmogorov-Smirnov statistic')
        plt.xlabel('Dimension')
        plt.title(distance[3])
        plt.legend()
        plt.savefig(distance[2])
        plt.show()

#firstOnes()


def secondRound(data = data):

    plt.figure(figsize=(20, 14))
    plt.figure(1)

    # all vocabulary
    plt.subplot(211)
    plt.title('All the vocabulary')
    plt.ylabel('Kolmogorov-Smirnov statistic')
    try:
        for distance in data:
            plt.plot(x_axis, distance[0], 'bo', linestyle='-', label=distance[4], c=distance[5])
    except:
        print('Something has happend :( \n')
    plt.legend()
    # just WordNet
    plt.subplot(212)
    plt.title('Just WordNet words')
    plt.ylabel('Kolmogorov-Smirnov statistic')
    plt.xlabel('Dimension')
    try:
        for distance in data:
            plt.plot(x_axis, distance[1], 'ro', linestyle='-', label=distance[4], c=distance[5])
    except:
        print('Something has happend :( \n')
    plt.legend()
    plt.savefig('All distances, all frameworks')
    plt.show()

secondRound()

