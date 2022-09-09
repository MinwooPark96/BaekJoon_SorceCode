import sys
input=sys.stdin.readline
N,M,B=map(int,input().split(" "))
count=N*M
inventory=B
List=[]
for _ in range(N):
    new=list(map(int,input().split(" ")))
    List+=new

List.sort(reverse=True)

maxh=(sum(List)+B)//count
minh=min(List)

mintime=1e9
minheight=1e9

for height in range(maxh,minh-1,-1):
    time=0
    for block in List:
        difference=block-height
        
        if difference>0:
            time+=difference*2
            inventory+=difference
        else :
            time+=abs(difference)
            inventory-=difference
        ###
        if inventory < 0:
            break
    if time<mintime:
        mintime=time
        minheight=height
    elif time==mintime:
        if height>minheight:
            mintime=time
            minheight=height
print(mintime,minheight)

            

