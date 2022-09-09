## insert sort

n=int(input())
List=[]
for _ in range(n):
    List.append(int(input()))

#List=[5,4,3,1,2,-1,423,2,-3,-100,2,17]
#List=[1]


for i in range(1,n):
    for j in range(i):
        if List[j]>List[i]:
            List[j],List[i]=List[i],List[j]
for i in List:
    print(i)

