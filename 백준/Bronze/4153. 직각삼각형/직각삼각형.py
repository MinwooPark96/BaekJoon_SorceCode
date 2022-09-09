def discriminator(inputs:list)->str:
    
    inputs.sort()
    check=inputs[0]**2+inputs[1]**2
    
    if check==inputs[2]**2:
        print("right")
    else :
        print("wrong")

List=[]
while 1:
    new=list(map(int,input().split(" ")))
    if not sum(new):
        break
    List.append(new)
for i in List:
    discriminator(i)

