import copy
n=int(input())
maxList=[0 for i in range(n)]
for i in range(1,n+1):# i=1~n
    new=list(map(int,input().split(" ")))
    if i==1: #만약 첫 층이라면
        maxList[0]=new[0]
        continue
    premaxList=copy.deepcopy(maxList)
    for j in range(i):
        
        if j==0:#첫째항과 마지막항은
            maxList[j]=premaxList[0]+new[0] #새로운 값을 더해주고 완료
        elif j==i-1:#첫째항과 마지막항은
            maxList[j]=premaxList[j-1]+new[-1] #새로운 값을 더해주고 완료
        else:
            maxList[j]=max(premaxList[j],premaxList[j-1])+new[j]
        
print(max(maxList))