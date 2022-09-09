n=int(input())
List=list(map(int,input().split(" ")))

dp=[0 for i in List]
dp[0]=1

for curidx in range(1,n): #1~n

    for preidx in range(0,curidx): #0~n-1
        
        if List[curidx]>List[preidx]: #현재의 값보다 작으면
            
            if dp[curidx]<dp[preidx]:
                
                dp[curidx]=dp[preidx]
    dp[curidx]+=1

print(max(dp))