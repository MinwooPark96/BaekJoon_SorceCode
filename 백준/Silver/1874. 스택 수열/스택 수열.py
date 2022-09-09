n=int(input())
orient=[]
for _ in range(n):
    orient.append(int(input()))

element=[i+1 for i in range(n)]
mystack=[-1]
top=0
Answer=[]
unsolve=False

while orient:
    orientnum=orient.pop(0)
    if orientnum>top:
        while orientnum!=top:
            top=element.pop(0)
            mystack.append(top)
            #print("+")
            Answer.append("+")
        mystack.pop(-1)
        top=mystack[-1]
        #print("-")
        Answer.append("-")
    elif orientnum==top:
        mystack.pop(-1)
        top=mystack[-1]
        #print("-")
        Answer.append("-")
    else:
        unsolve=True
        break

if unsolve:
    print("NO")
else:
    for i in Answer:
        print(i)