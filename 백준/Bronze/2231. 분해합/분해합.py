
n=int(input())

def sepsum(k:int)->int:
    result=k
    while k!=0:
        result+=k%10
        k=k//10
    return result

mydic={i:sepsum(i) for i in range(n)}

result=[]
for i in mydic:
    if mydic[i]==n:
        result.append(i)

if not result:
    print(0)
else :
    print(min(result))