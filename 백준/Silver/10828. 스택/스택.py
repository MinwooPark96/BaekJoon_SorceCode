class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack():
    def __init__(self):
        self.storesize=0
        self.sentinel=Node(999)
    def push(self,val):
        newNode=Node(val)
        newNode.next=self.sentinel.next
        self.sentinel.next=newNode
        
        self.storesize+=1
    def pop(self):
        if self.sentinel.next:
            print(self.sentinel.next.val)
            self.sentinel.next=self.sentinel.next.next
            self.storesize-=1
            
        else:
            print(-1)
    def size(self):
        print(self.storesize)
    def empty(self):
        if self.storesize:
            print(0)
        else:
            print(1)
    def top(self):
        if self.sentinel.next:
            print(self.sentinel.next.val)
        else:
            print(-1)

n=int(input())
my_stack=Stack()
commandlist=[]
for _ in range(n):
    commandlist.append(list(input().split(" ")))

for command in commandlist:
    if command[0]=="push":
        my_stack.push(int(command[1]))
    elif command[0]=="pop":
        my_stack.pop()
    elif command[0]=="top":
        my_stack.top()
    elif command[0]=="empty":
        my_stack.empty()
    elif command[0]=="size":
        my_stack.size()

