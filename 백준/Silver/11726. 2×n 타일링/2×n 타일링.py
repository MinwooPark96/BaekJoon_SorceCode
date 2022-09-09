n=int(input())
List=[0,1,2]
for i in range(3,n+1):
    List.append(List[i-1]+List[i-2])

if n<=2:
    print(n)
else:
    print(List[-1]%10007)