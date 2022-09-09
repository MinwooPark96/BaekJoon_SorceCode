import sys
input=sys.stdin.readline
N=int(input())
List=list(map(int,input().split(" ")))
#List=[4,1,5,2,3]
List.sort()
def Binarysearch(List:list,x:int)->int:
    start=0
    end=len(List)-1
    while start<=end:
        mid=(start+end)//2
        if List[mid]==x:
            return 1
        elif List[mid]>x:
            end=mid-1
        else :
            start=mid+1
   
    return 0
M=int(input())
searchList=list(map(int,input().split(" ")))
for i in searchList:
    print(Binarysearch(List,i))