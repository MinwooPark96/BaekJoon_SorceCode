def gcd(a,b):
    M=max(a,b)
    m=min(a,b)
    r=0
    while m!=0:
        r=M%m
        M=m
        m=r
    return M

n,m=map(int,input().split(" "))
g=gcd(n,m)
print(g)
print(int(n*m/g))