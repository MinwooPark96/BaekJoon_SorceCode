n=int(input())
score=list(map(int,input().split(" ")))
score
maxnum=max(score)
result=(100*sum(score))/(n*maxnum)
print(result)