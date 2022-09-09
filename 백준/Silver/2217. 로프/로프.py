n=int(input())
List=[]
for _ in range(n):
    List.append(int(input()))
    
List.sort()
count=n
preweight=-1
while List:
    minvalue=List.pop(0) #최소길이의 루프 추출
    maxweight=minvalue*count #최대 중량 계산
    if maxweight>=preweight: #이전까지의 최대중량보다 크다면 최신화
        preweight=maxweight
    count-=1
print(preweight)