n=int(input())
List=list(map(int,input().split(" ")))

List.sort()
answer=List[0]*List[-1]
print(answer)