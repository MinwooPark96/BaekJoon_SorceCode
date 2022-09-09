n=int(input())
dp=[[0]*11 for _ in range(n+1)]
dp[1]=[0]+[1]*9+[9]
dp
for i in range(2,n+1):
    for j in range(0,11): #dp[i][10] : 계단수의 갯수
        if j==0:
            dp[i][j]=dp[i-1][j+1]
        elif j==9:
            dp[i][j]=dp[i-1][j-1]
        elif j==10:
            dp[i][j]=2*dp[i-1][j]-dp[i-1][0]-dp[i-1][9]
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
print(dp[-1][-1]%1000000000)