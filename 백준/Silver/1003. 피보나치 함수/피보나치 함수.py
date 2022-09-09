dic={0:[1,0],1:[0,1]}
n=int(input())
List=[]
for _ in range(n):
    List.append(int(input()))
maxnum=max(List)
for i in range(2,maxnum+1):
    dic[i]=[dic[i-1][0]+dic[i-2][0],dic[i-1][1]+dic[i-2][1]]
for i in List:
    print(dic[i][0],dic[i][1])