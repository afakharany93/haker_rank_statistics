import math

def mean(x):
    n = len(x)
    return sum(x)/n
def std(x):
    n = len(x)
    mue = mean(x)
    numerator = sum(map(lambda x: (x-mue)**2, x))
    return math.sqrt(numerator/n)

def covariance(x,y):
    mean_x = mean(x)
    mean_y = mean(y)
    n = len(x)
    return sum(map(lambda x_i, y_i: (x_i-mean_x)*(y_i-mean_y), x, y))/n

def pearson_correl_coeff(x,y):
    return covariance(x,y)/(std(x)*std(y))

if __name__ == '__main__':
    n = float(input())
    X = list(map(float, (input()).split()))
    Y = list(map(float, (input()).split()))
    pcc = pearson_correl_coeff(X,Y)
    print(round(pcc, 3))
