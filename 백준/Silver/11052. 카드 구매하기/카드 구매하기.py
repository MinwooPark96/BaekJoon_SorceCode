n=int(input())
p=[0]+list(map(int,input().split()))
dp=[0 for i in range(n+1)]

for t in range(1,n+1):#전체 덩어리길이
    for m in range(1,t+1): #현재 덩어리길이
        dp[t]=max(dp[t],dp[t-m]+p[m])
print(max(dp))