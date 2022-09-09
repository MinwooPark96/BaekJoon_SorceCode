import copy
n=int(input())
matrix=[[0,0,0]]

for _ in range(n):
    new=list(map(int,input().split(" ")))
    matrix.append(new)
ow={0:[1,2],1:[0,2],2:[0,1]}

pre=copy.deepcopy(matrix[1])
for i in range(2,n+1):
    cur=copy.deepcopy(matrix[i])
    for j in range(0,3):
        cur[j]=min(cur[j]+pre[ow[j][0]],cur[j]+pre[ow[j][1]])
    pre=copy.deepcopy(cur)
print(min(cur))