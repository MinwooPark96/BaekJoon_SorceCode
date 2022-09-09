# 소인수분해 하였을 때, 2,3,5 가 1개 이상 있어야함.
# 10의 배수 중 3의 배수를 찾는게 빠를듯.

N=input()
if not "0" in set(N):
    print(-1)
else:
    numList=list(map(int,list(N)))
    numList.sort()
    numList.pop(0) 
    #이제 numList 의 조합중 합하여 3의 배수를 만들 수 있는지 확인하면 됨.
    answer=0
    if not sum(numList)%3:
        for i in numList[::-1]:
            answer=10*answer+i
        print(answer*10)
    else :
        print(-1)
# Idea
# 3의 배수는 각 자리수의 합이 3의 배수임
# 10의 배수는 끝자리에 0 이 붙어있음