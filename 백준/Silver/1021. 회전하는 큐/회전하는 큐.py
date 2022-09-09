class node():
    def __init__(self,val):
        self.val=val
        self.next=None

class circle():
    def __init__(self):
        self.sentinel=node(1)
        self.size=1
        self.move=0
        self.latest=self.sentinel
        
    def push(self,val):
        newnode=node(val)
        newnode.next=self.sentinel
        self.latest.next=newnode
        self.latest=newnode
        
        self.size+=1
    
    def pop(self,val):
        try:
            curNode=self.curNode
        except:
            curNode=self.sentinel
        if self.size==1:
            return
        
        elif curNode.val==val:
            while curNode.next.val!=val:
                curNode=curNode.next
            curNode.next=curNode.next.next
            self.curNode=curNode.next
            self.size-=1
        else:
            curmove=0
            while curNode.next.val!=val:
                curNode=curNode.next
                curmove+=1
            curNode.next=curNode.next.next
            curmove+=1
            self.move+=min(curmove,self.size-curmove)
            self.size-=1
            self.curNode=curNode.next
        
        
        
my_circle=circle()
n,m=map(int,input().split())
for i in range(1,n):
    my_circle.push(i+1)

delList=list(map(int,input().split()))
for i in delList:
    my_circle.pop(i)

print(my_circle.move)      