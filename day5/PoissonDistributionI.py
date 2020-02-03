import math

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def poisson(mean, k):
    return mean**k * math.exp(-1*mean)/factorial(k)

if __name__ == '__main__':
    mean = float(input())
    k = int(input())
    prop = poisson(mean, k)
    print(round(prop,3))
