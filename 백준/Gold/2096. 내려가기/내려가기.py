import sys

inut=sys.stdin.readline
n=int(input())
dp_max = [0,0,0]
dp_min = [0,0,0]
for _ in range(n):
    a,b,c = map(int,input().split())
    #max
    x = max(dp_max[0]+a,dp_max[1]+a)
    y = max(dp_max[0]+b,dp_max[1]+b,dp_max[2]+b)
    z = max(dp_max[1]+c,dp_max[2]+c)
    
    #min
    q = min(dp_min[0]+a,dp_min[1]+a)
    k = min(dp_min[0]+b,dp_min[1]+b,dp_min[2]+b)
    r = min(dp_min[1]+c,dp_min[2]+c)
    
    dp_max=[x,y,z]
    dp_min=[q,k,r]

print(max(dp_max),min(dp_min))