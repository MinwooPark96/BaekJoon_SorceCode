import sys
input=sys.stdin.readline
rank=0
n=int(input())
dic={}
List=list(map(int,input().split(" ")))
sortedList=sorted(List)
rank=0
for i in sortedList:
    if dic.get(i)!=None:
        pass
    else:
        dic[i]=rank
        rank+=1
for i in List:
    print(dic[i],sep=" ",end=" ")