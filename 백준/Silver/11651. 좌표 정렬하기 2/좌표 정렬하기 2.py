n=int(input())
List=[]
for _ in range(n):
    List.append(list(map(int,input().split(" "))))

List.sort(key=lambda x:x[0])
List.sort(key=lambda x:x[1])
for i in List:
    print(i[0],i[1])