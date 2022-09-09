def beeHouse(N):
    value=1 
    term=6
    group=1
    
    if N==1:
        return group
    while N>value:
        value+=term
        group+=1
        term+=6
    return group

N=int(input())
print(beeHouse(N))