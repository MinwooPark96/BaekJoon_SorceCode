def gcd(a,b):
    M=max(a,b)
    m=min(a,b)
    r=0
    while m!=0:
        r=M%m
        M=m
        m=r
    return M
checklist=[]
n=int(input())
for _ in range(n):
    l=list(map(int,input().split(" ")))
    checklist.append(l)
for i in range(n):
    g=gcd(checklist[i][0],checklist[i][1])
    lcm=int(checklist[i][0]*checklist[i][1]/g)
    print(lcm)

