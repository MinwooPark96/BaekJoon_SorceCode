
n=int(input())
dic={}
ageList=[]
for _ in range(n):
    new=input().split(" ")
    age,name=int(new[0]),new[1]
    if dic.get(age):
        dic[age].append(name)
    else:
        dic[age]=[name]
        ageList.append(age)
ageList.sort()
for i in ageList:
    while dic[i]:
        print(i,dic[i].pop(0))