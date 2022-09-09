import math
import sys
input=sys.stdin.readline
def discriminant(n:int)->bool:
    #if n is prime, return true
    if n==1 : 
        return False
    elif n==2 or n==3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def checknum(n:int)->int:
    count=0
    for i in range(n+1,2*n+1):
        if discriminant(i):
            count+=1
    return count

numlist=[]
while 1:
    n=int(input())
    if n==0:
        break
    numlist.append(n)
for i in numlist:
    print(checknum(i))