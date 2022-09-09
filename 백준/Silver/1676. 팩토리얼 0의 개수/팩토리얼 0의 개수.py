n=int(input())
facList=[1]
def factorial(n:int)->None:
    if n==1:
        return 
    for i in range(1,n+1):
        facList.append(i*facList[-1])
factorial(n)
interest=facList[-1]
count=0
while 1:
    r=interest%10
    if r!=0:
        break
    interest//=10
    count+=1
print(count)