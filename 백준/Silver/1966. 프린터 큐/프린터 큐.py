Answer=[]

def printerQueue(N,M):
    #N: 총 문서의 개수, M : M번째 원소의 출력 순서
    importance=list(map(int,input().split(" ")))
    maximportance=max(importance)
    dic={i:importance[i] for i in range(len(importance))}
    paper=[i for i in range(len(importance))]
    count=0
    deleted=-1

    while deleted!=M: #삭제되는 인덱스와 M이 같다면
        popping=paper.pop(0)
        if dic[popping]==maximportance:
            dic[popping]=-1
            maximportance=max(dic.values())
            deleted=popping
            count+=1
        else:
            paper.append(popping)
    Answer.append(count)
    
n=int(input())

inputs=[]
for _ in range(n):
    N,M=map(int,input().split(" "))
    printerQueue(N,M)
    
for i in Answer:
    print(i)