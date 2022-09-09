def Shift(x:int)->str:
    return bin(x)[2:]

def Add(x:int,y:int)->int:
    X=Shift(x);Y=Shift(y)
    n=len(X);m=len(Y)
    difference=n-m
    if difference>0:
        Y="0"*difference+Y
    else:
        X="0"*(-1*difference)+X
    length=max(n,m)
    store="0"
    result=""
    for i in range(length-1,-1,-1):
        
        cursum=int(X[i])+int(Y[i])+int(store)
        
        if cursum<=1:
            result=str(cursum)+result
            store="0"
        elif cursum==2:
            result="0"+result
            store="1"
        else:
            result="1"+result
            store="1"
    
    if store=="1":
            result="1"+result
    answer=0
    weight=1
    for i in range(len(result)):
        answer+=int(result[-1-i])*weight
        weight*=2
    return answer

a,b=map(int,input().split(" "))
print(Add(a,b))