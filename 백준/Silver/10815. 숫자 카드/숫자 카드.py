n=int(input());s1=list(map(int,input().split(" ")))
m=int(input());s2=list(map(int,input().split(" ")))

s1=set(s1)

for i in s2:
    if i in s1:
        print(1,end=" ")
    else:
        print(0,end=" ")