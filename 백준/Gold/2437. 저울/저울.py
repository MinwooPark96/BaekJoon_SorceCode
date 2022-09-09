n=int(input())
#List=[3,1,6,2,7,30,1]
List=list(map(int,input().split()))
List.sort()
sumvalue=0
for i in range(0,n):
    if List[i]>sumvalue+1:
        break
    else:
        sumvalue+=List[i]
print(sumvalue+1)
# 오름차순 정렬 후 지금까지 봐왔던 값들의 합 보다 큰 값을 마주하면 지금까지의 합과 그값 사이의 공백을 채울 수 없다.
# 지금까지의 값들의 합이 최대로 만들 수 있는 값이다.
# 순차 적으로 위 과정을 하면 멈추기 전까지는 모든 값을 만들 수 있다.