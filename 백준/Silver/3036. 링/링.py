
def gcd(a:int,b:int):
    M=max(a,b)
    m=min(a,b)
    r=0
    while m!=0:
        r=M%m
        M=m
        m=r
    return M

def frac(a:int,b:int): #a/b
    m=gcd(a,b)
    print(int(a/m),"/",int(b/m),sep="")

n=int(input())
l=list(map(int,input().split(" ")))
for i in range(1,n):
    frac(l[0],l[i])