import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
my_queue=deque()
commandlist=[]
for _ in range(n):
    commandlist.append(list(input().rstrip().split(" ")))

for command in commandlist:
    if command[0]=="push":
        my_queue.append(int(command[1]))
    elif command[0]=="pop":
        try:
            x=my_queue.popleft()
            print(x)
        except:
            print(-1)
    elif command[0]=="front":
        try:
            print(my_queue[0])
        except:
            print(-1)
    elif command[0]=="back":
        try:
            print(my_queue[-1])
        except:
            print(-1)
    elif command[0]=="empty":
        if len(my_queue):
            print(0)
        else:
            print(1)
    elif command[0]=="size":
        print(len(my_queue))



