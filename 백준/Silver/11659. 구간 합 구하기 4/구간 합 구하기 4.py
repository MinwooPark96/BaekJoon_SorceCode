import sys
# N : 숫자 갯수, M: 합을 계산할 갯수
input=sys.stdin.readline

N,M=map(int,input().split(" "))
List=list(map(int,input().split(" ")))
for i in range(len(List)):
    if i!=0:
        List[i]+=List[i-1]
Dict={i:List[i-1] for i in range(1,N+1)}
Dict[0]=0
Answer=[]
for _ in range(M):
    i,j=map(int,input().split(" "))
    Answer.append(Dict[j]-Dict[i-1])
for i in Answer:
    print(i)