n,k=map(int,input().split(" "))

choose=[[0]*(k+2) for i in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i==j:
            choose[i][j]=1
        if j==0:
            choose[i][j]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        choose[i][j]=choose[i-1][j-1]+choose[i-1][j]

print(choose[n][k]%10007)