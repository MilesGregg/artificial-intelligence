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

def step(r, w):
    summation = w[0]
    for i in range(len(r)-1):
        summation += w[i+1] * r[i]
    return 1.0 if summation >= 0.0 else 0.0

if __name__ == "__main__":
    iterations = 10000
    rate = 0.0001

    weights = [0.0 for i in range(len(data[0]))]

    for i in range(iterations):
        for row in data:
            error = row[-1] - step(row, weights)
            weights[0] = weights[0] + rate * error
            for j in range(len(row)-1):
                weights[j + 1] = weights[j + 1] + rate * error * row[j]
                
    print(weights)
