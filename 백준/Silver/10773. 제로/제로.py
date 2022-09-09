n=int(input())
List=[0]
for _ in range(n):
    new=int(input())
    if new==0:
        List.pop(-1)
    else:
        List.append(new)
print(sum(List))