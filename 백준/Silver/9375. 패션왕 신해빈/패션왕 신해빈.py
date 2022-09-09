Answer=[]
def fasion(n):
    global Answer
    dic={}
    for _ in range(n):
        a,b=input().split(" ")
        if dic.get(b):
            dic[b]+=1
        else :
            dic[b]=1
    answer=1
    for i in dic:
        answer*=dic[i]+1
    if n==0:
        return 0
    return answer-1

n=int(input())
for _ in range(n):
    k=int(input())
    print(fasion(k))

