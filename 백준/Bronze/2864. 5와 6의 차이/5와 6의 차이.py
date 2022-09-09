inputs=input()
mins=sum(list(map(int,inputs.replace("6","5").split(" "))))
maxs=sum(list(map(int,inputs.replace("5","6").split(" "))))
print(mins,maxs)

