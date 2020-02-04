import math

def standard_normal_distribution(x):
    return math.exp(-x**2 / 2) / math.sqrt(2*math.pi)

def normal_distribution(x, mean, std):
    return standard_normal_distribution((x-mean)/std)/std

def cumulative_distribution(x, mean, std):
    erf_value = math.erf((x-mean)/(std*math.sqrt(2)))
    return 0.5*(1+erf_value)

def bounded_cumulative(a,b, mean,std):
    return cumulative_distribution(b, mean, std) - cumulative_distribution(a, mean, std)

def clt_distribution(x,n,mean,std):
    mean_dash = n*mean
    std_dash = math.sqrt(n)*std
    return normal_distribution(x, mean_dash, std_dash)

def clt_cumulative_distribution(x,n,mean,std):
    mean_dash = n*mean
    std_dash = math.sqrt(n)*std
    return cumulative_distribution(x, mean_dash, std_dash)

def clt_bounded_cumulative(a,b,n, mean,std):
    mean_dash = n*mean
    std_dash = math.sqrt(n)*std
    return bounded_cumulative(a,b, mean_dash,std_dash)

def prediction_interval(mean,std,z):
    return mean-z*std, mean+z*std

if __name__ == '__main__':
    # max_load = float(input())
    n = float(input())
    mean = float(input())
    std = float(input())
    middle_percentage = float(input())
    z = float(input())
    # mean_dash = n*mean
    std_dash = std/math.sqrt(n)
    L,U = prediction_interval(mean,std_dash,z)
    print(round(L,4))
    print(round(U,4))
