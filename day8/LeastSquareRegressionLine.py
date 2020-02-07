from sklearn import linear_model
import numpy as np

'''
xl = [1, 2, 3, 4, 5]
x = np.asarray(xl).reshape(-1, 1)
y = [2, 1, 4, 3, 5]
lm = linear_model.LinearRegression()
lm.fit(x, y)
print(lm.intercept_)
print(lm.coef_[0])
'''
if __name__ == '__main__':
    X = []
    Y = []
    for i in range(5):
        x,y = list(map(float, (input()).split()))
        X.append(x)
        Y.append(y)
    lm = linear_model.LinearRegression()
    X = np.asarray(X).reshape(-1, 1)
    lm.fit(X,Y)
    p = lm.predict(np.asarray([80]).reshape(-1, 1))
    # print(p)
    print(round(p[0],3))
