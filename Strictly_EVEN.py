a=int(input())
b=[int(x) for x in input().split()]
c=[]
f=0
for i in (range(len(b))):
    if i%2==0 and b[i]%2==0:
        f=f+1
for i in b:
    if i%2==0:
        c.append(i)
if f>=len(c):
    print(True)
else:
    print(False)