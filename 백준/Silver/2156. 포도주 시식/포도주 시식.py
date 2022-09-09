n=int(input())

score=[0]
for i in range(n):
    score.append(int(input()))
matrix=[[0]*3 for i in range(n+1)]

matrix[1][1]=score[1]
try:
    matrix[2][0]=score[1]+score[2]
    matrix[2][1]=0
    matrix[2][2]=score[2]
except:
    pass
for i in range(2,n+1):
    matrix[i][2]=max(matrix[i-1][0],matrix[i-1][1],matrix[i-2][0],matrix[i-2][1]) #현재 위치에 있는 포도주를 안먹는 상태
    matrix[i][1]=matrix[i-1][2]+score[i] 
    matrix[i][0]=matrix[i-1][1]+score[i] #다음 포도주를 먹을 수 없는 상태
print(max(matrix[-1]))

