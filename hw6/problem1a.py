import math
from matplotlib import pyplot as plt
import numpy as np
from sklearn import tree

data = np.array([
    [1, 0, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1],
    [1, 1, 0]
])

weights = np.array([0, 0, 0, 1, 1])

def gini(data, weights, index):
    zeros = 0
    ones = 0

    for val in data[:, index]:
        if val == 0: 
            zeros += 1

    for val in data[:, index]:
        if val == 1:
            ones += 1

    zero_weights_for_zeros = 0
    zero_weights_for_ones = 0
    ones_weights_for_zeros = 0
    ones_weights_for_ones = 0

    for val in weights[data[:, index] == 0]:
        if val == 0: 
            zero_weights_for_zeros += 1

    for val in weights[data[:, index] == 0]:
        if val == 1:
            zero_weights_for_ones += 1


    for val in weights[data[:, index] == 1]:
        if val == 0: 
            ones_weights_for_zeros += 1

    for val in weights[data[:, index] == 1]:
        if val == 1:
            ones_weights_for_ones += 1

    return zeros * (1 - math.pow(zero_weights_for_zeros / zeros, 2) - \
                    math.pow(zero_weights_for_ones / zeros, 2)) / weights.shape[0] + \
            ones * (1 - math.pow(ones_weights_for_zeros / ones, 2) - \
                    math.pow(ones_weights_for_ones / ones, 2)) / weights.shape[0]

for i in range(len(data[1])):
    print(gini(data, weights, i))

_, ax = plt.subplots()
tree.plot_tree(tree.DecisionTreeClassifier(criterion = 'gini').fit(data, weights), ax = ax, filled = True, feature_names = ['A_1', 'A_2', 'A_3'])
plt.show()
