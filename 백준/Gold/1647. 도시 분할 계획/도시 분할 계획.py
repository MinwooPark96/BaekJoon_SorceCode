from collections import deque

## 1647 번


class edge():
    def __init__(self,v1,v2,weight):
        self.v1=v1
        self.v2=v2
        self.weight=weight
parent=list()    
#parent 함수는 입력과 함께 해야 한다.
def getparent(x:int)->int:
    if parent[x]==x:
        return x
    return getparent(parent[x])

def unionparent(x:int,y:int)->None: #직접적으로 입력을 받는 부분
    parent_x=getparent(x)
    parent_y=getparent(y)
    if parent_x>parent_y:
        parent[parent_x]=parent_y
    else :
        parent[parent_y]=parent_x

def findparent(x:int,y:int)->bool:
    parent_x=getparent(x)
    parent_y=getparent(y)
    if parent_x!=parent_y:
        return True
    return False

V,E=map(int,input().split(" "))

parent=[i for i in range(V+1)]
edges=[]

for _ in range(E):
    v1,v2,weight=map(int,input().split(" "))
    edges.append(edge(v1,v2,weight))
    
edges.sort(key=lambda x : x.weight)
edge_count=0
answer=list()
mst=list()
for i in range(E):
    if edge_count>=V-2:
        break
    cur_edge=edges[i]    
    if findparent(cur_edge.v1,cur_edge.v2):
        answer.append(cur_edge)
        mst.append(cur_edge.weight)
        edge_count+=1
        unionparent(cur_edge.v1,cur_edge.v2)
        
print(sum(mst))