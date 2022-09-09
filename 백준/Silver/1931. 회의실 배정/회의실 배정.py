import sys
input=sys.stdin.readline
n=int(input())
List=[]
for i in range(n):
    List.append(tuple(map(int,input().split(" "))))
#List=[(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,13),(12,14)]
List.sort(key=lambda x: x[0])
List.sort(key=lambda x: x[1])
startpoint=List[0][0]
endpoint=List[0][1]
Answer=[List[0]]
for i in range(1,n):
    if List[i][0]>=endpoint:
        startpoint=List[i][0]
        endpoint=List[i][1]
        Answer.append(List[i])
print(len(Answer))   

