def gcd(a,b):
    a=max(a,b)
    b=min(a,b)
    r=0
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def compiler(l:tuple):
    a=l[0];b=l[1]
    if gcd(a,b)==1:
        print("neither")
    else :
        if a>b:
            print("multiple")
        else :
            print("factor")
checklist=[]
while 1:
    newTuple=(tuple(map(int,input().split(" "))))
    if newTuple[0]==0:
        break
    checklist.append(newTuple)
for i in checklist:
    compiler(i)