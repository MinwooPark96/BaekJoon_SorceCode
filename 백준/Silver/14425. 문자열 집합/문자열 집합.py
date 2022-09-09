n,m=map(int,input().split(" "))
S=set()
M=[]
for _ in range(n):
    S.add(input())
for _ in range(m):
    M.append(input())
count=0
for i in M:
    if i in S:
        count+=1

print(count)