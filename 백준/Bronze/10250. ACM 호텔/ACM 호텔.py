#YYXX
n=int(input())
info=[]
for _ in range(n):
    info.append(list(map(int,input().split(" "))))
for i in range(n):
    H,W,N=info[i][0],info[i][1],info[i][2]
    X=(N-1)//H+1
    Y=(N-1)%H+1
    if X<10:
        print(str(Y)+"0"+str(X))
    else :
        print(str(Y)+str(X))

