A,B,V=map(int,input().split(" "))

day=(V-A)//(A-B)
region=day*(A-B)
#(A-B)*n<V<=(A-B)*n+A => answer is n+1
# 전날까지 올라간거리 < V <= 오늘 올라간거리

while True:
    day+=1
    region+=A
    if region>=V:
        break
    region-=B

if day>=0:
    print(day)
else :
    print(1)