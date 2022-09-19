n=int(input())
maxlen=0
dic={}
visit={}
for _ in range(n):
    string=list(input())
    digit=len(string)-1
    for i in range(digit+1):
        if dic.get(string[i]):
            dic[string[i]]+=10**digit
        else:
            dic[string[i]]=10**digit
        digit-=1
numList=[9-i for i in range(len(dic))]
visit={i:False for i in dic}
length=len(visit)
maxnum=0
def permutation(depth,curnum,length):
    global maxnum
    if depth==length:
        if curnum>maxnum:
            maxnum=curnum
    else:
        for alpha in dic:
            if not visit[alpha]:
                visit[alpha]=True
                curnum+=numList[depth]*dic[alpha]
                permutation(depth+1,curnum,length)
                visit[alpha]=False
                curnum-=numList[depth]*dic[alpha]

permutation(0,0,length)
print(maxnum)