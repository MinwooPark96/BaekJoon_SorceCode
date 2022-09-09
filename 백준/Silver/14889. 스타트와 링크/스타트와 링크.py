import copy

n=int(input())

people=[i+1 for i in range(n)]
visit={i:False for i in people}
Group=[]
def backtrack(group,curmax=0):
    if len(group)==len(people)//2:
        result=copy.deepcopy(group)
        Group.append(result)
        return(group)

    for i in people:      
        if i>curmax:
            curmax=i
            group.append(i)
            backtrack(group,curmax)
            group.pop(-1)
            
backtrack([])
N=len(Group)

def teamscore(group1,group2,score):
    score1=0
    score2=0
    n=len(group1)
    for i in range(n):
        for j in range(n):
            score1+=score[group1[i]][group1[j]]
            score2+=score[group2[i]][group2[j]]
    return abs(score1-score2)


score=[[0]*(n+1)]
for i in range(n):
    row=[0]+list(map(int,input().split(" ")))
    score.append(row)
answer=[]
for i in range(N//2):
    answer.append(teamscore(Group[i],Group[N-1-i],score))
print(min(answer))