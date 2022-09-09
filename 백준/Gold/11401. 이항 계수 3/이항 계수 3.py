p=1_000_000_007

n,k=map(int,input().split())

def factorial(n):
    global p
    if n==0 or n==1:
        return 1
    result=1
    for i in range(2,n+1):
        result=(result*i)%p
    return result

def modulepow(n,k,p):
    value=n
    result=1
    while k!=0:
        if k%2:
            result=(result*value)%p
        k//=2
        value=(value*value)%p
    return result

first=factorial(n)%p
second=modulepow(factorial(k),p-2,p)
third=modulepow(factorial(n-k),p-2,p)
result=(first*second*third)%p
print(result)