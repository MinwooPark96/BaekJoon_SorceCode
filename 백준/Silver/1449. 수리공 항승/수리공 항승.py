n,L=map(int,input().split())
point=list(map(int,input().split()))

point.sort()
#do
interest=point.pop(0)
end=interest+L
count=1
#end 미만까지만 커버가능
while point:
    interest=point.pop(0)
    if interest<end:
        continue
    else:
        end=interest+L
        count+=1
print(count)

