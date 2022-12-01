from sys import setrecursionlimit, stdin
from collections import deque

setrecursionlimit(10 ** 6)
input=stdin.readline
n=int(input())

def DFS(v:int):
        global time
        if not visit[v]:
            visit[v]=1
            time+=1
            time_checker[v].append(time)
            for next_v in child[v]:
                DFS(next_v)

            time+=1
            time_checker[v].append(time)
            finish_stack[time]=v

def DFS_T(v:int):
        if not visit_T[v]:
            visit_T[v]=1
            scc_element.append(v)
            for next_v in child_T[v]:
                DFS_T(next_v)

for _ in range(n):
    N,M=map(int,input().split())
    child={i:[] for i in range(1,N+1)}
    child_T={i:[] for i in range(1,N+1)}
    for _ in range(M):
        v1,v2=map(int,input().split())
        child[v1].append(v2)
        child_T[v2].append(v1)
    time_checker={i:[] for i in range(1,N+1)}
    visit=[0 for i in range(N+1)]
    visit_T=[0 for i in range(N+1)]
    scc=[]

    time=0
    finish_stack=[0 for i in range(2*N+1)]
    
    for v in range(1,N+1):
        DFS(v)
    # finish_stack[time] = vertex number

    for f_time in range(2*N,0,-1):
        v=finish_stack[f_time]
        if v:
            scc_element=[]
            DFS_T(v)
            if scc_element:
                scc.append(scc_element)



    scc_v={i+1: scc[i] for i in range(len(scc))}
    v_scc=dict()
    for i in scc_v:
        for j in scc_v[i]:
            v_scc[j]=i

    child_scc={i:set() for i in scc_v}
    for v in scc_v:
        
#         for c in child[v]:
#             if v_scc[c]!=v:
#                 child_scc[v].add(v_scc[c])
        for c in scc_v[v]:
            for cc in child[c]:
                if v_scc[cc]!=v:
                    child_scc[v].add(v_scc[cc])
    indegree=[0 for i in range(len(scc_v)+1)]

    for i in child_scc:
        for j in child_scc[i]:
            indegree[j]+=1

    indegree[0]=1
    print(indegree.count(0))
