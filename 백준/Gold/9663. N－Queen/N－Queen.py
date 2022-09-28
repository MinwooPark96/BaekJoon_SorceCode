import copy
from collections import deque
n=int(input())
visit=[0 for i in range(n)]
queen=deque()
result=0
def Back(visit,depth=0):
    global result
    global n
    if depth>=n:
        result+=1
        return
    
    for i in range(n):
        if not visit[i]: 
            pre=visit 
            visit=[0 for i in range(n)]
            queen.append(i)
            for j in range(len(queen)): 
                visit[queen[j]]=1
                if queen[j]+(depth-j)+1<n:
                    visit[queen[j]+(depth-j)+1]=1
                if queen[j]+j-depth-1>=0:
                    visit[queen[j]+j-depth-1]=1
            
            Back(visit,depth+1)
            
            queen.pop()
            
            visit=pre

Back(visit,0)
print(result)