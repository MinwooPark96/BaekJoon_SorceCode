n,k,m=map(int,input().split())
answer=1

while k:
    if k%2:
        answer*=n%m
    k//=2
    n=n*n%m
print(answer%m)