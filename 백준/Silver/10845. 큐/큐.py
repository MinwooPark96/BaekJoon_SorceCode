#import sys
#input=sys.stdin.readline #쓰면 틀림
class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class queue():
    def __init__(self):
        self.storesize=0
        self.sentinel=Node(-1) #센티널값을 -1로 설정
    
    def push(self,val): #센티넬의 next 에 새로운 노드 추가.
        self.storesize+=1
        
        newNode=Node(val)
        newNode.next=self.sentinel.next #기존의 첫 노드 앞에 새로운 노드 추가
        self.sentinel.next=newNode #새로운 노드를 샌티널 노드 앞에 두기
    
    def pop(self):
        curNode=self.sentinel
        if self.sentinel.next: #노드가 존재한다면
            while curNode.next.next: #pop하려는 노드의 앞노드로 이동후
                curNode=curNode.next
            print(curNode.next.val)
            curNode.next=None #pop하려는 노드의 앞노드의 다음노드를 None으로 교체
    
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
    
    def back(self):
        if self.sentinel.next: 
            print(self.sentinel.next.val)
        
        else:
            print(self.sentinel.val)
    
    def front(self):
        
        if self.sentinel.next:
            curNode=self.sentinel
            while curNode.next:
                curNode=curNode.next
            print(curNode.val)
        
        else:
            print(self.sentinel.val)
n=int(input())
my_queue=queue()
commandlist=[]
for _ in range(n):
    commandlist.append(list(input().split(" ")))

for command in commandlist:
    if command[0]=="push":
        my_queue.push(int(command[1]))
    elif command[0]=="pop":
        my_queue.pop()
    elif command[0]=="front":
        my_queue.front()
    elif command[0]=="back":
        my_queue.back()
    elif command[0]=="empty":
        my_queue.empty()
    elif command[0]=="size":
        my_queue.size()



