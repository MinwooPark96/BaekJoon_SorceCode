import sys
input=sys.stdin.readline

n,m=map(int,input().split(" "))
empty=[0 for i in range(n+1)]
cumrows=[empty]
for _ in range(n):
    row=[0]+list(map(int,input().split(" ")))
    cumrow=[0]
    for i in range(1,n+1):
        cumrow.append(row[i]+cumrow[i-1])
    cumrows.append(cumrow)

Answer=[]
for _ in range(m):
    points=list(map(int,input().split(" ")))
    rowstart=points[0]
    rowend=points[2]
    colstart=points[1]
    colend=points[3]
    
    answer=0
    for i in range(rowstart,rowend+1):
        answer+=cumrows[i][colend]-cumrows[i][colstart-1]
    Answer.append(answer)
for i in Answer:
    print(i)