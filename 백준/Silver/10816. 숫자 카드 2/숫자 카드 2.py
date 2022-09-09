import sys
input=sys.stdin.readline
n=int(input());s1=list(map(int,input().split(" ")))
m=int(input());s2=list(map(int,input().split(" ")))

s1_dic={}
for i in s1:
    if s1_dic.get(i):
        s1_dic[i]+=1
    else:
        s1_dic[i]=1

for i in s2:
    if s1_dic.get(i):
        print(s1_dic[i],end=" ")
    else:
        print(0,end=" ")
    