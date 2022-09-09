def myfunction():
    string=input()
    dic={}
    num=1
    for i in string:
        if dic.get(i):
            pass
        else :
            dic[i]=num
            num+=1
    List=[dic[i] for i in string]
    for i in range(1,len(string)):
        temp=List[i]-List[i-1]
        if temp<0:
            return 0
    return 1
n=int(input())
answer=0
for _ in range(n):
    x=myfunction()
    answer+=x
print(answer)