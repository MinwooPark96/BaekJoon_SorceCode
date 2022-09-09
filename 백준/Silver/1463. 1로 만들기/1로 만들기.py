n=int(input())
List=[0 for i in range(n+1)]

for i in range(2,n+1):
    if not i%2: #2의배수라면
        if not i%3: #3의배수라면
            List[i]=min(List[i//2],List[i//3],List[i-1])+1
        else:
            List[i]=min(List[i//2],List[i-1])+1
    else: #2의배수가 아니라면
        if not i%3: #3의배수라면
            List[i]=min(List[i//3],List[i-1])+1
            
        else:
            List[i]=List[i-1]+1
print(List[-1])