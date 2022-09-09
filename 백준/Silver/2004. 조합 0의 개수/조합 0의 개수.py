import sys
input=sys.stdin.readline
n,m=map(int,input().split(" "))

def count(n):
    #n!을 소인수 분해 하였을 때 2와 5의 갯수 구하기.
    count_2=0
    count_5=0
    curnum=2
    interest=n
    while interest>=curnum:
        count_2+=interest//curnum
        curnum*=2
    curnum=5
    interest=n
    while interest>=curnum:
        count_5+=interest//curnum
        curnum*=5
    return count_2,count_5

over=count(n)
behind1=count(m)
behind2=count(n-m)
answer=min(over[0]-(behind1[0]+behind2[0]),over[1]-(behind1[1]+behind2[1]))
print(answer)