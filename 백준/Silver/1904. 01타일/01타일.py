n=int(input())
List=[1,2]
def call(n):
    if n==1:
        return 1
    for i in range(2,n):
        Newinput=List[1]+List[0]
        if Newinput>=15746:
            Newinput%=15746
        List.append(Newinput)
        List.pop(0)
        
    return List[-1]
print(call(n))