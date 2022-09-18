n=int(input())
unsigned=[]
signed=[]
countzero=0

for i in range(n):
    num=int(input())
    if num>0:
        unsigned.append(num)
    elif num<0:
        signed.append(num)
    else:
        countzero+=1

answer=0
signed.sort(reverse=False)
unsigned.sort(reverse=True)
while len(signed)>1:
    x=signed.pop(0)
    y=signed.pop(0)
    answer+=x*y

while countzero:
    if signed:
        signed.pop(0)
        countzero-=1
    else :
        break
answer+=sum(signed)

while len(unsigned)>1:
    x=unsigned.pop(0)
    y=unsigned.pop(0)
    if x!=1 and y!=1:
        answer+=x*y
    else:
        answer+=x+y
answer+=sum(unsigned)

print(answer)