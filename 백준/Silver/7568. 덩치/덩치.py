n=int(input())
#n=5
#List=[(55,185),(58,183),(88,186),(60,175),(46,155)]
List=[]
for i in range(n):
    List.append(tuple(map(int,input().split(" "))))
def compare(A:tuple,B:tuple)->all:
    #if we can't compare each people, return -1
    #else return more big person (0 or 1)
    
    if (A[0]-B[0])*(A[1]-B[1])<=0:
        return -1
    if A[0]+A[1]>B[0]+B[1]:
        return 0
    return 1

rank={i:1 for i in range(n)}

for i in range(n-1):
    for j in range(i+1,n):
        com=compare(List[i],List[j])
        if com==0:
            rank[j]+=1
        elif com==1:
            rank[i]+=1

for i in rank.values():
    print(i,end=" ")