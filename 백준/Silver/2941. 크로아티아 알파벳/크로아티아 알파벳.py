string=input()

alphaset=["c=","c-","dz=","d-","lj","nj","s=","z="]

count=0
for i in alphaset:
    
    if string.count(i):
        count+=string.count(i)
        string=string.replace(i,' ')
    
strlist=string.split()
string=""
for i in strlist:
    string+=i

if string:
    count+=len(string)
    print(count)
else :
    print(count)

