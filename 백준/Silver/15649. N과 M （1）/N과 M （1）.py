def permutation(depth,n,m):
    ##Basis Term
    if depth==m:
        for i in answer:
            print(i,end=" ")
        print()
        return
    for i in range(1,n+1): # i를 시작으로 하는 백트레킹
        
        if not visited[i]: # i를 방문한적이 없다면,
            visited[i]=True #방문 체크하고
            answer.append(i) #answer 에 i 추가하고
            permutation(depth+1,n,m) # 다음 depth 로 내려감.
            ###위에서 stack and call 구조로 방문체크하고 append 하며 하부구조로 내려감.
            
            visited[i]=False #다음 단계를 위해 다시 초기화하는 과정.
            answer.pop() #다음 단계를 위해 다시 초기화하는 과정.
n,m=map(int,input().split(" "))
visited=[False for _ in range(n+1)]
answer=[]
permutation(0,n,m)