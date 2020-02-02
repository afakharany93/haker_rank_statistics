def geo_prop(n , p):
    q = 1-p
    return q**(n-1) * p

if __name__ == "__main__":
    p1,p2 = map(float, (input()).split())
    p = p1/p2
    n = int(input())
    prop = map( lambda y : geo_prop(y,p), range(1,n+1))

    print(round(sum(prop),3))
