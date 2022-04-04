from matplotlib import pyplot as plt
from sklearn import tree

data = [
    [1, 0, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1],
    [1, 1, 0]
]
weights = [0, 0, 0, 1, 1]

_, ax = plt.subplots()
tree.plot_tree(tree.DecisionTreeClassifier(criterion = 'entropy').fit(data, weights), ax = ax, filled = True, feature_names = ['A_1', 'A_2', 'A_3'])
plt.show()
