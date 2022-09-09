n,m=map(int,input().split(" "))
A_set=set()
B_set=set()
for _ in range(n):
    A_set.add(input())
for _ in range(m):
    B_set.add(input())

A_set.intersection_update(B_set)
Answer=sorted(list(A_set))
print(len(Answer))
for i in Answer:
    print(i)