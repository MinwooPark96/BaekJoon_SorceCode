import sys
#input=sys.stdin.readline
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
V=int(input())
alpha="A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z".strip().split(',')
alphabet=[i.strip() for i in alpha]

int_alpha=dict(enumerate(alphabet,1))
alpha_int={int_alpha[i]:i for i in int_alpha.keys()}

get=[0 for i in range(V+1)]
Nodes=[None for i in range(V+1)]


for _ in range(V):
    inputs=input().split()
    int_inputs=[]
    for v in inputs:
        if v=='.':
            int_inputs.append(-1)
        else :
            int_inputs.append(alpha_int[v])
            
    
    for v in int_inputs:
        if v==-1:
            continue
        elif get[v]==0:
            get[v]=1
            Nodes[v]=Node(v)
    
    v,l,r=int_inputs
    if l!=-1:
        Nodes[v].left= Nodes[l]
    if r!=-1:
        Nodes[v].right=Nodes[r]
root=Nodes[1]


def Traversal(curNode,t=0):
    if t==0:
        print(int_alpha[curNode.value],end='')
    
    if curNode.left:
        Traversal(curNode.left,t)
    
    if t==1:
        print(int_alpha[curNode.value],end='')
    
    if curNode.right:
        Traversal(curNode.right,t)
    
    if t==2:
        print(int_alpha[curNode.value],end='')
    
Traversal(root,0)
print()
Traversal(root,1)
print()
Traversal(root,2)
