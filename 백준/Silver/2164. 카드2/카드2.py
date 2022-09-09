from typing import Deque
n=int(input())
l=Deque([i+1 for i in range(n)])
while len(l)!=1:
    l.popleft()
    x=l.popleft()
    l.append(x)
    
print(l[0])