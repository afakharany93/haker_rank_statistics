import math

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def poisson(mean, k):
    return mean**k * math.exp(-1*mean)/factorial(k)

def poisson_expectation_squared(mean):
    return mean+ mean**2

if __name__ == '__main__':
    mean_a, mean_b = map(float, (input()).split())
    expectation_a = poisson_expectation_squared(mean_a)
    expectation_b = poisson_expectation_squared(mean_b)
    cost_a = 160 + 40*expectation_a
    cost_b = 128 + 40*expectation_b
    print(round(cost_a,3))
    print(round(cost_b,3))
    # k = int(input())
    # prop = poisson(mean, k)
    # print(round(prop,3))
