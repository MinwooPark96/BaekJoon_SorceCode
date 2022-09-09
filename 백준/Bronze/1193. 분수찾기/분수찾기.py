#group:[start,end]
#1:[1,1],2:[2,3],3:[4,5,6],4:[7,8,9,10],...

n=int(input())

# First. which group contain n'th element?
# If n=12, 1+2+3+4<n<=1+2+3+4+5. So n is 5'th group

def sumk(k): #sum of 1~k
    return k*(k+1)//2

k=1
while n>sumk(k):
        k+=1

# where k is group of n.
# we want direction of reading table.
# It is easy to think that 
# if a/b in k'th group, a+b=k+1 
# and direction is right top to left bottom if k is even.
# direction is reversed when we read from last element of the group.

cur=sumk(k)

if k%2==0: #If k is even,
    point=[k,1]
    while cur!=n:
        point[0]-=1;point[1]+=1
        cur-=1
else :
    point=[1,k]
    while cur!=n:
        point[0]+=1;point[1]-=1
        cur-=1

print(point[0],"/",point[1],sep="")