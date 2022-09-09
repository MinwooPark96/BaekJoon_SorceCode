
def Hanoi(n,start=1,end=3,info=[]):
    
    if n==1:
        info.append((start,end))
        return 1
    
    else :
        l=[1,2,3]
        l.remove(start)
        l.remove(end)
        
        mid=l[0]
    
        a=Hanoi(n-1,start,mid,info)
        
        info.append((start,end))
        
        b=Hanoi(n-1,mid,end,info)
        
        result=a+b+1
        
        return result

info=[]
n=int(input())
print(Hanoi(n,1,3,info))
for i in info:
    print(str(i[0])+" "+str(i[1]))

