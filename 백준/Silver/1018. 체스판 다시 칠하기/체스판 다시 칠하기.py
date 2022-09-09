import copy
def preprocess(List):
    shift={"B":1,"W":0}
    for i in range(len(List)):
        for j in range(len(List[0])):
            List[i][j]=shift[List[i][j]]
    return List

def FilterSum(List:list)->int: #8x8 list

    base=[[0]*8 for _ in range(8)]
    filter_1=copy.deepcopy(base)
    filter_2=copy.deepcopy(base)

    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                filter_1[i][j]=1
            else :
                filter_2[i][j]=1
    sum_1=0
    sum_2=0
    for i in range(8):
        for j in range(8):
            sum_1+=bool(List[i][j]-filter_1[i][j])#원소의 차이가 존재한다면 +=1
            sum_2+=bool(List[i][j]-filter_2[i][j])
    return min(sum_1,sum_2) #필터와 다른 원소의 갯수(수정해야하는)

def sliding(List:list,n:int,m:int)->int:
    result=[]
    for i in range(n-8+1):
        for j in range(m-8+1):
            interest=[k[j:j+8] for k in List[i:i+8]]
            curmin=FilterSum(interest)
            result.append(curmin)
    return min(result)

n,m=map(int,input().split(" "))
List=[]
for _ in range(n):
    string=input()
    List.append(list(string))

List=preprocess(List)
print(sliding(List,n,m))