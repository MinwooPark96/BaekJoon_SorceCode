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
n=int(input())

while not discriminant(n):
    if n==1:
        break
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            n//=i
            print(i)
            break
if n!=1:
    print(n)