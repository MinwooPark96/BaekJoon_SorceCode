string=input()
check=string.split("-",1)
inminus=False
if len(check)!=1:
    inminus=True

def stringTolist(string):
    string=string.replace("+"," ").replace("-"," ")
    try:
        return list(map(int,string.split(" ")))
    except:
        return []
if not inminus:
    print(sum(stringTolist(check[0])))
else:
    answer=[]
    for i in check:
        answer.append(sum(stringTolist(i)))
    print(answer[0]-answer[1])