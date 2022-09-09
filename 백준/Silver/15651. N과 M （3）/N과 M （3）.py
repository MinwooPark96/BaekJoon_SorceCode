#n=4;m=2
n,m=map(int,input().split(" "))
answer=[]
def permutation(depth):
    global n
    global m
    if depth==0:
        for i in answer:
            print(i,end=" ")
        print()
        return
    for i in range(1,n+1):
        answer.append(i)
        permutation(depth-1)
        ###stack and call until basis term
        answer.pop()
permutation(m)