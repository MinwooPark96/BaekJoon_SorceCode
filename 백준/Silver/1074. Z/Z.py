#2^N 행렬에서 (r,c)을 몇번째로 방문하였을 까?


def twopow(n:int):# 2^n:
    binary_str=bin(n)[2:]
    length=len(binary_str)
    numList=[]
    temp=2
    for i in range(length):
        numList.append(temp)
        temp*=temp
    result=1
    for i in range(length):
        if binary_str[::-1][i]=="1":
            result*=numList[i]
    return result

def Group(N,r,c):#r,c가 몇군인가?
    if r>=twopow(N-1): 
        if c>=twopow(N-1):
            return 4
        else:
            return 3
    else:
        if c>=twopow(N-1):
            return 2
        else:
            return 1

count=0

def Zfunction(N,r,c):
    global count
    if N==0:
        return 
    group=Group(N,r,c)
    temp=twopow(N-1)
    count+=temp*temp*(group-1)
    Zfunction(N-1,r%temp,c%temp)

N,r,c=map(int,input().split(" "))
Zfunction(N,r,c)
print(count)