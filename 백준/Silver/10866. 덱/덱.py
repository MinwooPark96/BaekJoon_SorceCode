class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class Deque():
    def __init__(self):
        self.storesize=0
        self.sentinel=Node(-1)
    
    def push_front(self,val): #센티넬의 next 에 새로운 노드 추가.
        self.storesize+=1
        
        newNode=Node(val)
        newNode.next=self.sentinel.next
        self.sentinel.next=newNode
    
    def push_back(self,val): #센티넬의 next 에 새로운 노드 추가.
        self.storesize+=1
        
        curNode=self.sentinel
        while curNode.next!=None:
            curNode=curNode.next
        curNode.next=Node(val)
    
    def pop_back(self):
        curNode=self.sentinel
        if self.sentinel.next:
            while curNode.next.next:
                curNode=curNode.next
            print(curNode.next.val)
            curNode.next=None
    
            self.storesize-=1

        else:
            print(-1)
    
    def pop_front(self):
        if self.sentinel.next: #센티넬 다음원소가 존재한다면
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
    
    def front(self):
        if self.sentinel.next:
            print(self.sentinel.next.val)
        
        else:
            print(self.sentinel.val)
    
    def back(self):
        
        if self.sentinel.next:
            curNode=self.sentinel
            while curNode.next:
                curNode=curNode.next
            print(curNode.val)
        
        else:
            print(self.sentinel.val)

n=int(input())
my_deque=Deque()
commandlist=[]
for _ in range(n):
    commandlist.append(list(input().split(" ")))

for command in commandlist:
    if command[0]=="push_back":
        my_deque.push_back(int(command[1]))
    elif command[0]=="push_front":
        my_deque.push_front(int(command[1]))
    elif command[0]=="pop_back":
        my_deque.pop_back()
    elif command[0]=="pop_front":
        my_deque.pop_front()
    elif command[0]=="front":
        my_deque.front()
    elif command[0]=="back":
        my_deque.back()
    elif command[0]=="empty":
        my_deque.empty()
    elif command[0]=="size":
        my_deque.size()



