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
n=int(input())
nums=list(map(int,input().split(" ")))
count=0
for i in range(n):
    count+=discriminant(nums[i])
print(count)