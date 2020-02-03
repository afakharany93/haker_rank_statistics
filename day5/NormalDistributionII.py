import math

def standard_normal_distribution(x):
    return math.exp(-x**2 / 2) / math.sqrt(2*math.pi)

def normal_distribution(x, mean, std):
    return standard_normal_distribution((x-mean)/std)/std

# def erf(z):
#     integration = sum(map(lambda x: math.exp(-1*x**2), range(int(z)+1)))
#     return 2*integration(z)/math.sqrt(math.pi)

def cumulative_distribution(x, mean, std):
    erf_value = math.erf((x-mean)/(std*math.sqrt(2)))
    return 0.5*(1+erf_value)

def bounded_cumulative(a,b, mean,std):
    return cumulative_distribution(b, mean, std) - cumulative_distribution(a, mean, std)

if __name__ == '__main__':
    mean, std = map(float, (input()).split())
    higher_limit = float(input())
    lower_limit = 0
    prop1 = 1- bounded_cumulative(lower_limit, higher_limit, mean,std)
    higher_limit = float(input())
    prop2 = 1-bounded_cumulative(lower_limit, higher_limit, mean,std)
    # higher_limit = lower_limit
    # lower_limit = 0
    prop3 = bounded_cumulative(lower_limit, higher_limit, mean,std)
    print(round(prop1*100, 2))
    print(round(prop2*100, 2))
    print(round(prop3*100, 2))
