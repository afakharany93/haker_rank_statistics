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

def n_elements_less_than_equal_value_in_list (element, x):
    x = list(set(x))
    filtered_list = list(filter(lambda y: y<= element, x))
    return len(filtered_list)

def ranking(x):
    return list(map(lambda y: n_elements_less_than_equal_value_in_list (y, x), x))

def spearman_rank_corel(x,y,n):
    rank_x = ranking(x)
    rank_y = ranking(y)
    diff = sum(map(lambda a,b: (a-b)**2, rank_x,rank_y))
    return 1 -  (6*diff)/(n*(n**2 - 1))

if __name__ == '__main__':
    n = float(input())
    X = list(map(float, (input()).split()))
    Y = list(map(float, (input()).split()))

    rs = spearman_rank_corel(X,Y,n)
    print(round(rs,3))
