#List=[10,-4,3,1,5,6,-35,12,21,-1]
n=int(input())
List=list(map(int,input().split(" ")))

PASL=[List[0]] #partial accumulate sum list.
for i in range(1,n):
    PASL.append(max(PASL[i-1]+List[i],List[i])) #PASL[k] (where k=1~i) List[:i] 까지 읽었을때 누적합과 현재값중 큰녀석.
    #현재값이 더 커지면 현재값이 append 되므로 거기서 부터 합하기 시작함.
    #어디서부터 초기화되는지 우리는 관심없음.
    
print(max(PASL))