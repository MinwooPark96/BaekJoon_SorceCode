
n=input()
n_list=list(n)
changer=[]
for i in n_list:
  changer.append(int(i)**5)

print(sum(changer))