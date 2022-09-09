n=int(input())
change=1000-n

answer=0
coin=[500,100,50,10,5,1]
while change:
    for i in coin:
        answer+=change//i
        change=change%i
print(answer)

