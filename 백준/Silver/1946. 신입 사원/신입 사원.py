
import sys
input=sys.stdin.readline
def recruit(n:int):
    List=[]
    for _ in range(n):
        List.append(list(map(int,input().split(" "))))
    List.sort(key=lambda x:x[0])
    List=[List[i][1] for i in range(n)]
    count=0
    maxrank=List[0]
    for i in range(1,n):
        if List[i]>maxrank:
            count+=1
        else:
            maxrank=List[i]
    return count
#4562713

n=int(input())
Answer=[]
for _ in range(n):
    k=int(input())
    Answer.append(k-recruit(k))
for i in Answer:
    print(i)



