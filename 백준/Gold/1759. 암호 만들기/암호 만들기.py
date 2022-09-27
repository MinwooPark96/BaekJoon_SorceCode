n,m=map(int,input().split())
alpha=input().split()
alpha.sort()
visit=[False for i in range(m)]
aeiou=set("aeiou")
Answer=[]
def Back(depth=0,pw="",count_ae=0):
    global n
    if depth==n:    
        check_aeiou=set(pw)
        if len(check_aeiou.intersection(aeiou))>=1 and len(check_aeiou.difference(aeiou))>=2:
            Answer.append(pw)
    for i in range(len(visit)):
        try:
            check=ord(pw[-1])<ord(alpha[i])
        except:
            check=1
        if not visit[i] and check:
            visit[i]=True
            pw+=alpha[i]
            Back(depth+1,pw,count_ae)
            pw=pw[:-1]
            visit[i]=False
            
        
    
Back(0,"")
for i in Answer:
    print(i)