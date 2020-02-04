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
    erf_value = math.erf((x-mean_dash)/(std_dash*math.sqrt(2)))
    return 0.5*(1+erf_value)
def clt_bounded_cumulative(a,b,n, mean,std):
    mean_dash = n*mean
    std_dash = math.sqrt(n)*std
    return cumulative_distribution(b, mean_dash, std_dash) - cumulative_distribution(a, mean_dash, std_dash)

if __name__ == '__main__':
    max_load = float(input())
    n = float(input())
    mean = float(input())
    std = float(input())
    prop = clt_bounded_cumulative(0,max_load,n, mean,std)
    # prop = clt_cumulative_distribution(max_load,n,mean,std)
    print(round(prop,4))
