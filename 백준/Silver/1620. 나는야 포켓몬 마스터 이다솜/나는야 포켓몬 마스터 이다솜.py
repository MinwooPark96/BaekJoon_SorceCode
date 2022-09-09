N,M=map(int,input().split(" "))
ptoc={}
for i in range(N):
    ptoc[input()]=i+1
ctop={ptoc[i]:i for i in ptoc}

Answer=[]
for _ in range(M):
    q=input()
    try :
        q=int(q)
        Answer.append(ctop[q])
    except:
        Answer.append(ptoc[q])
for i in Answer:
    print(i)