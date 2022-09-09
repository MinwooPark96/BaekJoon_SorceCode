n,m=map(int,input().split(" "))
memo={}
for _ in range(n):
    address,password=input().split(" ")
    memo[address]=password
Answer=[]
for _ in range(m):
    Answer.append(memo[input()])
for i in Answer:
    print(i)
    