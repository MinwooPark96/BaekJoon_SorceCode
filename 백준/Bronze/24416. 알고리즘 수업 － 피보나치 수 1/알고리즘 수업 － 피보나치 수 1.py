n=int(input())
l=[1,1]

def call(n):
    if n==1 or n==2:
        return 1
    else :
        return call(n-1)+call(n-2)
print(call(n),n-2)