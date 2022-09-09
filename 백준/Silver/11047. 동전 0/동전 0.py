import sys
input=sys.stdin.readline
n,k=map(int,input().split(" "))

money=[]
for _ in range(n):
    money.append(int(input()))

count=0
while money:
    coin=money.pop(-1)
    if coin<=k:
        while coin<=k:
            count+=1
            k-=coin
print(count) 