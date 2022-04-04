from matplotlib import pyplot as plt
from sklearn import tree

data = [
    [1, 0, 1, 0, 0, 0], # A1
    [1, 0, 1, 1, 0, 0], # A2
    [1, 0, 1, 0, 1, 0], # A3
    [1, 1, 0, 0, 1, 1], # A4
    [1, 1, 1, 1, 0, 0], # A5
    [1, 0, 0, 0, 1, 1], # A6
    [1, 0, 0, 0, 1, 0], # A7
    [0, 1, 1, 1, 0, 1], # A8
    [0, 1, 1, 0, 1, 1], # A9
    [0, 0, 0, 1, 1, 0], # A10
    [0, 1, 0, 1, 0, 1], # A11
    [0, 0, 0, 1, 0, 1], # A12
    [0, 1, 1, 0, 1, 1], # A13
    [0, 1, 1, 1, 0, 0]  # A14
]

weights = [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]

_, ax = plt.subplots()
tree.plot_tree(tree.DecisionTreeClassifier(criterion = 'entropy').fit(data, weights), filled = True, ax = ax, feature_names = ['A_1', 'A_2', 'A_3', 'A_4', 'A_5', 'A_6', 'A_7', 'A_8', 'A_9', 'A_10', 'A_11', 'A_12', 'A_13', 'A_14'])
plt.show()
