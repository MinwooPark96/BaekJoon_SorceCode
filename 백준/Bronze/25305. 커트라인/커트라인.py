N,k=map(int,input().split(" "))
List=list(map(int,input().split(" ")))
#N=5;k=2
#List=[100,76,85,93,98]
#insert sort

for i in range(1,N):
    for j in range(i):
        if List[j]>List[i]:
            List[j],List[i]=List[i],List[j]

print(List[-k])


