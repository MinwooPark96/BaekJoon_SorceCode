import sys
input=sys.stdin.readline
A,B,C=map(int,input().split(" "))

#we want n s.t. A+nB<nC
# => A/(C-B)<n
try:
    n=A//(C-B)+1
    if n>=0:
        print(n)
    else:
        print(-1)
except :
    print(-1)