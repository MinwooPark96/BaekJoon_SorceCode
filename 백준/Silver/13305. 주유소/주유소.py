import sys
input=sys.stdin.readline

n=int(input())
length=list(map(int,input().split(" ")))+[0]
price=list(map(int,input().split(" ")))

total=0
minp=price[0]
for i in range(1,n):
    total+=minp*length[i-1]
    if price[i]<minp:
        minp=price[i]
print(total)