import math
import sys
input=sys.stdin.readline

n=int(input())
numlist=[]
for _ in range(n):
    numlist.append(int(input()))

maxnum=max(numlist)

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

primelist=[]
for i in range(2,max(numlist)):
    if discriminant(i):
        primelist.append(i)

primeset=set(primelist)

def Goldguess(N:int,primeset:set)->list:
    #x(even)=p+q => return [p,q]
    k=N//2
    for t in range(0,k+1):
        if k+t in primeset:
            if k-t in primeset:
                break
    print(k-t,k+t)

for i in numlist:
    Goldguess(i,primeset)
    