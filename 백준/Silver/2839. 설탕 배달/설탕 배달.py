n=int(input())

x=0
supx=n//3
t=0

while x<=supx:
    if (n+2*x)%5==0:
        t=(n+2*x)//5
        break
    x+=1

if t==0:
    print(-1)
else :
    print(t)