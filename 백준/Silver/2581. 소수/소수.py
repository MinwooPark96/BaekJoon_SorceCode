import math
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

M=int(input())
N=int(input())

minPrime=-1
sumPrime=0
for i in range(M,N+1):
    if discriminant(i):
        if minPrime==-1:
            minPrime=i
            sumPrime=0
        sumPrime+=i
if sumPrime:
    print(sumPrime)
print(minPrime)

