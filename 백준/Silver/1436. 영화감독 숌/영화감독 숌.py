n=int(input())
curnum=666
visit=[]

def check(x):
    x=str(x)
    if "666" in x:
        return True
    return False
epoch=1
while len(visit)!=n:
    if check(curnum):
        if not curnum in visit:
            visit.append(curnum)
            
    curnum+=1
print(visit[-1])  