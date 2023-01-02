import heapq
import sys
from collections import defaultdict
#input=sys.stdin.readline
n=int(input())
for _ in range(n):
    
    m=int(input())
    count=0
    pQ_min = list()
    pQ_max = list()
    
    patience1 = defaultdict(int) #최대힙에서 제거되었음을 표시
    patience2 = defaultdict(int) #최소힙에서 제거되었음을 표시
    
    for _ in range(m):
        operator,code = input().split()
        if operator == 'D' and count != 0:
            count-=1
            
            if code == '1' :
                interest = -1*heapq.heappop(pQ_max)
                while patience2[interest]!=0:
                    patience2[interest]-=1
                    interest = -1*heapq.heappop(pQ_max)
                
                patience1[interest]+=1
                
            else : #code == '-1'
                interest = heapq.heappop(pQ_min)
                while patience1[interest]!=0:
                    patience1[interest]-=1
                    interest = heapq.heappop(pQ_min)
                
                patience2[interest]+=1
                
                
        elif operator == "I": # I num
            count+=1
            heapq.heappush(pQ_max,-1 * int(code))
            heapq.heappush(pQ_min,int(code))
    
    if count != 0:
        max_num = -1 * heapq.heappop(pQ_max)
        while patience2[max_num]!=0:
            patience2[max_num]-=1
            max_num = -1*heapq.heappop(pQ_max)
        
        min_num = heapq.heappop(pQ_min)
        while patience1[min_num]!=0:
            patience1[min_num]-=1
            min_num = heapq.heappop(pQ_min)
                
        print(max_num,min_num)
    else:
        print('EMPTY')


