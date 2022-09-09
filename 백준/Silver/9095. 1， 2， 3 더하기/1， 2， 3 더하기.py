n=int(input())
List=[0,1,2,4]
numList=[]
for _ in range(n):
    numList.append(int(input()))
maxnum=max(numList)
if maxnum<=3:
    pass
else:
    for i in range(4,maxnum+1):
        List.append(List[i-1]+List[i-2]+List[i-3])
for i in numList:
    print(List[i])

