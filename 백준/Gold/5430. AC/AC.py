# R 을 마주하였을때 실제로 뒤집지 않고 뒤에서 pop 
# D 의 총 개수가 문자열의 갯수보다 크다면 error를 반환.
# R 의 총 개수가 홀수개이면 출력시 거꾸로 출력,
# R 의 총 개수가 짝수이면 바르게 출력
# 처음에는 pop(0), R을 마주하면 pop(-1)

def ACfunction(order:str,numList:list)->all:
    length=len(order)
    count_D=order.count("D")
    if count_D>len(numList):
        return "error"
    
    count_R=length-count_D
    forward=True
    
    for i in order:
        if i=="R":
            forward = not forward
        else:
            if forward:
                numList.pop(0)
            else:
                numList.pop(-1)
    if not forward:
        numList.reverse()
    return numList
Answer=[]
n=int(input())
for _ in range(n):
    order=input()
    k=int(input())
    try:
        numList=list(map(int,input()[1:-1].split(",")))
    except:
        numList=[]
    Answer.append(ACfunction(order,numList))
for i in Answer:
    print(str(i).replace(" ",""))