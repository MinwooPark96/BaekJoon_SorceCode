n,m=map(int,input().split())
package=[]
piece=[]
for _ in range(m):
    pa,pi=map(int,input().split())
    package.append(pa)
    piece.append(pi)

q=n//6
r=n%6
minpa=min(package)
minpi=min(piece)
if minpi*6<minpa:
    print(n*minpi)
else:
    print(min(minpa*q+minpi*r,minpa*(q+1)))