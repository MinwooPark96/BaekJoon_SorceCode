def generate(n):
    result=n
    for i in str(n):
        result+=int(i)
    return result


Non_self=set()
for i in range(1,10001):
    curnum=i
    while generate(curnum)<=10000:
        curnum=generate(curnum)
        Non_self.add(curnum)
Answer={i for i in range(1,10001)}
Answer.difference_update(Non_self)
Answer=list(Answer)
Answer.sort()
for i in Answer:
    print(i)