n=int(input())
def Sum(n):
    return n*(n+1)//2
#1,2 :1 
#3,4,5 : 2
#6,7,8,9 : 3 

value=1
while Sum(value)<=n:
    value+=1
print(value-1)