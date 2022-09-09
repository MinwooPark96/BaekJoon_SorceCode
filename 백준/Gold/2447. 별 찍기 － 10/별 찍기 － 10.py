import copy

n=int(input())

def point(n):
    if n==3:
        return [["1","1","1"],["1","0","1"],["1","1","1"]]
    else :
        t=int(n/3)
        pre=point(t)
        pre=[i*3 for i in pre]
        post=[]
        for i in range(3):
            post+=copy.deepcopy(pre)
        
        for i in range(t,2*t):
            for j in range(t,2*t):
                post[i][j]="0"
        return post

def compiler(L):
    length=len(L)
    changer={"1":"*","0":" "}
    for i in range(length):
        x=""
        for j in range(length):
            x+=changer[L[i][j]]
        print(x)

M=point(n)
compiler(M)