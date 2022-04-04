import math


data = [
    [1, 0, 1, 0, 0, 0, 1], # A1
    [1, 0, 1, 1, 0, 0, 1], # A2
    [1, 0, 1, 0, 1, 0, 1], # A3
    [1, 1, 0, 0, 1, 1, 1], # A4
    [1, 1, 1, 1, 0, 0, 1], # A5
    [1, 0, 0, 0, 1, 1, 1], # A6
    [1, 0, 0, 0, 1, 0, 0], # A7
    [0, 1, 1, 1, 0, 1, 1], # A8
    [0, 1, 1, 0, 1, 1, 0], # A9
    [0, 0, 0, 1, 1, 0, 0], # A10
    [0, 1, 0, 1, 0, 1, 0], # A11
    [0, 0, 0, 1, 0, 1, 0], # A12
    [0, 1, 1, 0, 1, 1, 0], # A13
    [0, 1, 1, 1, 0, 0, 0]  # A14
]

def predict(row, weights):
    summation = 0
    for i in range(0, len(row) - 1):
        summation += weights[i + 1] * row[i]
    return 1.0 if summation >= 0.0 else 0.0

if __name__ == "__main__":
    iterations = 100
    rate = 0.1

    weights = [0 for _ in range(len(data[0]))]

    for i in range(iterations):
        for row in data:
            prediction = predict(row, weights)
            for j in range(len(row)-1):
                weights[j + 1] = weights[j + 1] + (row[-1] - prediction) * row[j] * rate 
    
    print(f'Weights = {weights}\n')

    for row in data:
        prediction = predict(row, weights)
        print(f'Actual = {row[-1]}, Prediction = {prediction}')
