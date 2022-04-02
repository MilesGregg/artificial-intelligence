import math

def calc(K, e):
    summation = 0
    for i in range(int((K+1)/2), K):
        vec = math.factorial(K) / (math.factorial(i) * math.factorial(K-i))
        output = vec * math.pow(e, i) * math.pow(1 - e, K - i)
        summation = summation + output

    return summation


if __name__ == "__main__":
    K_array = [5, 10, 20]
    e_array = [0.1, 0.2, 0.4]

    for K in K_array:
        for e in e_array:
            print(f'K = {K}, ε = {e} - {calc(K, e)}')
