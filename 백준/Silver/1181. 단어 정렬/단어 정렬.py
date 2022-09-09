n=int(input())
List=[]
for _ in range(n):
    List.append(input())
List=list(set(List))
List.sort()
List.sort(key=lambda x : len(x))
for i in List:
    print(i)