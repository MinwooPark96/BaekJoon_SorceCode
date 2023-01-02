n,m = map(int,input().split())
son = [i for i in range(n,n-m,-1)]
mom = [i for i in range(1,m+1)]

a=1
b=1
for i in range(m):
    a*=son[i]
for i in range(m):
    b*=mom[i]
print(a//b)