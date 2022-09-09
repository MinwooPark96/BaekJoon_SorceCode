import sys
input=sys.stdin.readline
n=int(input())

numList=[0]*10001

maxnum=0

for _ in range(n):
    x=int(input())
    if x>maxnum :
        maxnum=x
    numList[x]+=1

for i in range(1,maxnum+1):
    if numList[i]!=0:
        for _ in range(numList[i]):
            print(i)