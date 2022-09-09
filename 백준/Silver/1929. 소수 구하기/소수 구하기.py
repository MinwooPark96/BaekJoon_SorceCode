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

M,N=map(int,input().split(" "))

for i in range(M,N+1):
    if discriminant(i):
        print(i)