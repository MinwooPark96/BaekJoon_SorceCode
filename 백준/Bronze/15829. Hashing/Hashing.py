n=int(input())
epsilon=1
rList=[]
r=31
temp=r

while epsilon<=n:
    rList.append(temp)
    temp**=2
    epsilon*=2

H=0
M=1234567891

string=input()
alphabet="abcdefghijklmnopqrstuvwxyz"
dic={alphabet[i]:i+1 for i in range(26)}

def cal(i):
    binomial=bin(i)[2:]
    count=0
    answer=1
    for i in binomial[::-1]:
        if i=="1":
            answer*=rList[count]
        count+=1
    return answer

for i in range(n):
    H+=dic[string[i]]*cal(i)%M
print(H%M)