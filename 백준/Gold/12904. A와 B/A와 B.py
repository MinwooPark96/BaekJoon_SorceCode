from collections import deque
S=input()
T=input()
deque_t=deque(T)
lens=len(S);lent=len(T)
orient=True
while lens!=lent:
    if orient:
        popchar=deque_t.pop()
    else:
        popchar=deque_t.popleft()
    lent-=1
    if popchar=="B":
        orient=not orient     
T=""
if orient:
    for i in deque_t:
        T+=i
else:
    for i in list(deque_t)[::-1]:
        T+=i

if S==T:
    print(1)
else:
    print(0)