n=int(input())
def check(string:str):
    List=[]
    for i in string:
    
        if i=="(":
            List.append(1)
        else:
            try : 
                List.pop(-1)
            except : 
                List.append(-1)
                break;

    if List:
        print("NO")
    else :
        print("YES")
stringlist=[]
for _ in range(n):
    stringlist.append(input())
for string in stringlist:
    check(string)