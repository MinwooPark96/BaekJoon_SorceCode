answer=[]
curmax=0
def sortchoose(depth,n,m,curmax):
    if depth==0:
        for i in answer:
            print(i,end=" ")
        print()
        
        return
    for i in range(1,n+1): #1~n
        if i>=curmax:
            answer.append(i)
            curmax=i
            sortchoose(depth-1,n,m,curmax)
            answer.pop()
            curmax=0
            
n,m=map(int,input().split(" "))
#n=4;m=3
sortchoose(m,n,m,curmax)