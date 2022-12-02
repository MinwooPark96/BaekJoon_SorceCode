import heapq
import sys
input=sys.stdin.readline
max_pQ=[]
min_pQ=[]
max_size=0
min_size=0
flag=0
step=0
n=int(input())
for _ in range(n):
    x=int(input())
    ##초기
    if max_size ==0 and min_size==0:
        heapq.heappush(min_pQ,x)
        min_size+=1
        print(x)
        continue
    else :
       
        if not flag: #flag ==0 -> left
            if min_pQ[0]>=x:
                heapq.heappush(max_pQ,-1*x)
                max_size+=1
            else:
                heapq.heappush(max_pQ,-1*(heapq.heappop(min_pQ)))        
                heapq.heappush(min_pQ,x)
                
            flag=1
        else: #flag == 1 -> right
            if -1*max_pQ[0]<=x:
                heapq.heappush(min_pQ,x)
                max_size+=1
            else:
                heapq.heappush(min_pQ,-1*(heapq.heappop(max_pQ)))
                heapq.heappush(max_pQ,-1*x)
                
            flag=0
    if step%2==1:
        print(min_pQ[0])
    else :
        print(-1*max_pQ[0])
    step+=1