n=int(input())
rev=0
c=0
if n<0:
    n=n*-1
    c+=1
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if c==1:
    print(-rev)
else:
    print(rev)