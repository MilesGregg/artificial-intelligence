import random
import math


output = {
    'bar': 20,
    'bell': 15,
    'lemon': 5,
    'cherry': 3
}

symbols = ['bar', 'bell', 'lemon', 'cherry']

def iteration():
    num_coins = 10
    num_plays = 0

    while num_coins > 0:
        num_coins = num_coins - 1
        num_plays = num_plays + 1
        
        games = [random.choice(symbols) for _ in range(3)]
        slot = games[0]
        len_games = len(games)

        if games.count('bar') == len_games or games.count('bell') == len_games or \
           games.count('lemon') == len_games or games.count('cherry') == len_games:
            num_coins = num_coins + output[slot]
        elif slot == 'cherry' and games[1] == 'cherry':
            num_coins = num_coins + 2
        elif slot == 'cherry':
            num_coins = num_coins + 1

    return num_plays


if __name__ == "__main__":
    iterations = 10000

    outputs = []
    for _ in range(iterations):
        outputs.append(iteration())
    outputs.sort()
    print("Iterations:", iterations)
    print("Mean:", sum(outputs) / iterations)
    print("Median:", outputs[math.floor(iterations/2)])
