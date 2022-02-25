import math
import random
import numpy as np 


class TSPHillClimbingAlgorithm:
    def __init__(self) -> None:
        pass

    def swap(self, input, i, j):
        output = input.copy()
        output[i] = input[j]
        output[j] = input[i]
        return output

    def get_length(self, grid, nodes):
        return sum(grid[nodes[i - 1]][nodes[i]] for i in range(len(nodes)))

    def hill_climbing(self, grid):
        length = len(grid)
        nodes = list(range(length))
        random.shuffle(nodes)

        adjacent_nodes = [self.swap(nodes, i, j) for i in range(length) for j in range(i + 1, length)]

        best_get_length = self.get_length(grid, adjacent_nodes[0])
        for adjacent_node in adjacent_nodes:
            if self.get_length(grid, adjacent_node) < best_get_length:
                best_get_length = self.get_length(grid, adjacent_node)
        return best_get_length


class TSPGeneticAlgorithm:
    def __init__(self) -> None:
        pass
    
    def mutate(self, path):
        for i in range(len(path)):
            if (random.random() < 0.01):
                path = self.swap(path, i, np.random.randint(0, len(path)))
        return path

    def swap(self, input, i, j):
        output = input.copy()
        output[i] = input[j]
        output[j] = input[i]
        
        return output

    def fitness(self, path, nodes):
        output = 0
        for index in range(1, len(path)):
            i = nodes[int(path[index - 1])]
            j = nodes[int(path[index])]
            output = output + math.sqrt(math.pow(i[0] - j[0], 2) + math.pow(i[1] - j[1], 2))
        
        return output

    def get_best_path(self, sizes, nodes):
        output = {}
        for i in range(len(sizes)):
            output[i] = self.fitness(sizes[i], nodes)
        return sorted(output.items(), key = lambda output : output[1])

    def crossover(self, a):
        first = [a[i] for i in range(int(random.random() * len(a)))]
        end = [i for i in a if i not in first]
        
        return first + end
    
    def genetic(self, grid):
        random_sizes = [list(random.sample([0, 1, 2, 3], 4)) for _ in range(500)]
        output = []
        
        for _ in range(1000):
            output = [i[0] for i in self.get_best_path(random_sizes, grid)]
            total = [output[i] for i in range(100)]
            
            chromosones = [random_sizes[i] for i in total]
            crossovers = [self.crossover(chromosones[i]) for i in range(len(chromosones)-1)]
            output = [self.mutate(i) for i in crossovers]

        return round(self.get_best_path(output, grid)[0][1], -1)


grid = [
    [0, 20, 30, 10],
    [20, 0, 10, 30],
    [30, 10, 0, 20],
    [10, 30, 20, 0]
]

hill = TSPHillClimbingAlgorithm()
print("Hill Climbing:", hill.hill_climbing(grid))

print()

genetic = TSPGeneticAlgorithm()
print("Genetic:", genetic.genetic(grid))
