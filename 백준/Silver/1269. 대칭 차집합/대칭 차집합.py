n,m=map(int,input().split(" "))
A_set=set(map(int,input().split(" ")))
B_set=set(map(int,input().split(" ")))

A_union_B=A_set.union(B_set)
A_interaction_B=A_set.intersection(B_set)

answer=A_union_B.difference(A_interaction_B)
print(len(answer))

