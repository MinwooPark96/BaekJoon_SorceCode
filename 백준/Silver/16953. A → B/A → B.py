def operator1(n):
    return n//2

def operator2(n):
    return (n-1)//10

#거꾸로 B->A를 구해보자

A,B=map(int,input().split(" "))
unsolve=False
count=1
while B>A:
    if B%10==1:
        B=operator2(B)
        count+=1
    else:
        if B%2:
            unsolve=True
            break
        else:
            B//=2
            count+=1
if B-A or unsolve:
    print(-1)
else:
    print(count)

