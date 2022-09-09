import copy
def discriminator(n:int)->str:
    List1=list(str(n))
    List2=copy.deepcopy(List1)
    List1.reverse()
    check=List1==List2
    if check:
        print("yes")
    else :
        print("no")

List=[]
while 1:
    new=int(input())
    if new==0:
        break
    List.append(new)
for i in List:
    discriminator(i)