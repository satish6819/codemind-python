def sd(n):
    t=n
    while n>0:
        r=n%10
        if r==0 or t%r!=0:
            return False
        n=n//10
    return True   
i=int(input())
m=int(input())
for i in range(i,m+1):
    if sd(i)==True:
        print(i,end=' ')