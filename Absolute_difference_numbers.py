n,no=map(int,input().split())
rev=0
sum1=0
rev1=0
sum2=0
count=no
temp=n
while(temp>0):
    r=temp%10
    rev=rev*10+r
    temp=temp//10
while(n>0):
    r=n%10
    if count==0:
        break
    sum1=sum1*10+r
    n=n//10
    count-=1
    
count=no
while rev>0:
    r=rev%10
    if count==0:
        break
    sum2=sum2*10+r
    rev=rev//10
    count=count-1
while sum1>0:
    r=sum1%10
    rev1=rev1*10+r
    sum1=sum1//10
if rev1>sum2:
    print(rev1-sum2)
else:
    print(sum2-rev1)