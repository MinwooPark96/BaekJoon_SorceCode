s=input()
n=len(s)
answer=set()
for i in range(n):
    for j in range(i+1,n+1):
        answer.add(s[i:j])
print(len(answer))