n = int(input())
inf = 10000002
dont_touch = set()
step = [inf for _ in range(inf)]
parent = [1 for _ in range(inf)]
step[1] = 0
step[3] = 1
step[2] = 1

for i in range(1,n):
    if i != inf :
        if step[i]+1 < step[2*i]:
            step[2*i] = step[i] + 1
            parent[2*i] = i
        
        if step[i]+1 < step[3*i]:
            step[3*i] = step[i] + 1
            parent[3*i] = i
        
        if step[i]+1 < step[i+1]:
            step[i+1] = step[i] + 1
            parent[i+1] = i
x = n
answer = [x]
while x != 1:
    x = parent[x]
    answer.append(x)
print(step[n])
for i in answer:
    print(i,end = ' ')