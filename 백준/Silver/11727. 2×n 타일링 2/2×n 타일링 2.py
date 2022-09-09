n=int(input())
List=[0,1,3]
for i in range(3,n+1):
    List.append(List[i-1]+2*List[i-2])
if n<=2:
    print(List[n])
else:
    print(List[-1]%10007)

