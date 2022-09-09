class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedNode():
    def __init__(self):
        self.size=0
        self.sentinel=Node(-1)
        self.latest=self.sentinel
        
    def push(self,val):
        self.size+=1
        newnode=Node(val)
        self.latest.next=newnode
        self.latest=newnode
        newnode.next=self.sentinel
    
    def yosepus(self,k):
        result=[]
        visit={i+1:False for i in range(self.size)}
        visit[-1]=True #센티널 방문은 True 체크
    
        curNode=self.sentinel
        for _ in range(n):
    
            for _ in range(k):#k칸씩 뛰어넘기
                
                if curNode.next.val==-1:#센티널은 뛰어넘기
                    curNode=curNode.next.next
                else:
                    curNode=curNode.next
                while visit[curNode.val]:#현재 노드가 방문한적 있다면 넘어가라
                    curNode=curNode.next
                
                
            visit[curNode.val]=True
            result.append(curNode.val)
        return result


n,k=map(int,input().split(" "))
cycle=LinkedNode()
for i in range(n):
    cycle.push(i+1)
answer=cycle.yosepus(k)
endele=answer.pop(-1)
print("<",end="")
for i in answer:
    print(i,end=", ")

print(endele,">",sep="",end="")