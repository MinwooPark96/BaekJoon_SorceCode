import copy
n=int(input())

score=[0]
for i in range(n):
    score.append(int(input()))
matrix=[[0]*3 for i in range(n+1)]
# matrix[i][j] : i계단 도달하였을 때 최고점수, j: 해당 위치에서 잔여 점프횟수
# 무조건 최대한 밟는게 이득임 그렇치만 매우큰 스텝을 위해 연속 점프 가능

# matrix[i][2]=matrix[i-1][0] #해당위치를 밟고있지 않음(건너뛸것임)
# matrix[i][1]=matrix[i-1][2]+cur[i]  #한 단계점프 후 위치
# matrix[i][0]=matrix[i-1][1]+cur[i]  #다음 계단을 밟을 수 없는 상태

matrix[1][1]=score[1]
try:
    matrix[2][0]=score[1]+score[2]
    matrix[2][1]=0
    matrix[2][2]=score[2]
except:
    pass
for i in range(2,n+1):
    matrix[i][2]=max(matrix[i-1][0],matrix[i-1][1])
    matrix[i][1]=matrix[i-1][2]+score[i]
    matrix[i][0]=matrix[i-1][1]+score[i]
print(max(matrix[-1][0],matrix[-1][1]))

