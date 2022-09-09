n=int(input())

total=[]

for _ in range(n):
    
    s=input()
    
    total.append(s)

answer=[]

Double=[]
for s in total:
    l=s.split("X")
    l=[i for i in l if i]
    Double.append(l)

def calculate(s):
    n=len(s)
    count=0
    while n!=0:
        count+=n
        n-=1
    return count

for i in Double:
    count=0
    for j in i:
        count+=calculate(j)
    answer.append(count)

for i in answer:
    print(i)