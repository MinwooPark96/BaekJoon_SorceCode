n,m=map(int,input().split(" "))
mylist=list(map(int,input().split(" ")))

cursum=0
mostsum=0

for i in range(n-2):
    for j in range(i+1,n):
        for k in range(j+1,n):
            cursum=sum([mylist[i],mylist[j],mylist[k]])
            if cursum>mostsum and cursum<=m :
                mostsum=cursum
            
                
print(mostsum)            


