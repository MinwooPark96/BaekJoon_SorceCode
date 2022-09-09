n=int(input())
count={}
D=True
while D:
    interest=n%10
    if n<10:
        D=False
    
    if count.get(interest): 
        count[interest]+=1
    else :
        count[interest]=1        
    n//=10

Answer=0
digit=1
for i in range(10):
    D=count.get(i)
    if D:
        for j in range(1,D+1):
            Answer+=digit*i
            digit*=10

print(Answer)

