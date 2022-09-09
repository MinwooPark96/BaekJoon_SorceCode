n=int(input())
my_info=[]
for _ in range(n):
    l=list(map(int,input().split(" ")))
    my_info.append(l)

#리스트를 입력받아 거리제곱을 도출
import math

def Distance(info:list)->float:
    result=math.sqrt((info[3]-info[0])**2+(info[4]-info[1])**2)
    return result

#두 점사이의 관계를 도출

def Relation(info:list) -> int:
    distance=Distance(info)
    r1=info[2]
    r2=info[-1]
    bigr=max(r2,r1)
    smallr=min(r2,r1)
    if distance==0 and r1==r2:
        return -1
    elif distance<r2+r1 and distance>bigr-smallr:
        return 2
    elif distance==r2+r1 or distance==abs(r2-r1):
        return 1
    else :
        return 0
 
    
for i in range(n):
    attendlist=my_info[i]
    print(Relation(attendlist))


