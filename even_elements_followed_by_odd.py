n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        print(i,end=' ')
for j in l:
    if j%2!=0:
        print(j,end=' ')