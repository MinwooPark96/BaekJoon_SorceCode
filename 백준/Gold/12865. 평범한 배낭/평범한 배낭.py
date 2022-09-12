
n,v=map(int,input().split())
List=[]
maxweight=0
for _ in range(n):
    thing=list(map(int,input().split()))
    List.append(thing)    
    if maxweight<thing[0]:
        maxweight=thing[0]
dp=[[0]*(v+1) for _ in range(n+1)]
for i in range(1,n+1):
    thing=List[i-1]
    weight=thing[0];value=thing[1]
    for j in range(1,v+1):
        if j>=weight:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][v])