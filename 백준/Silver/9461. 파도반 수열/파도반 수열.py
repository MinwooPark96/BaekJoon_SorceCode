n=int(input())
n_list=[]
for _ in range(n):
    n_list.append(int(input()))

def wavehalf(n):
    init=[1,1,1,2,2]
    if n<=5:
        return init[n-1]
    for i in range(5,n):
        init.append(init[0]+init[-1])
        init.pop(0)
    return init[-1]

for i in n_list:
    print(wavehalf(i))