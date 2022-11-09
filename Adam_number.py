n = int(input())
sq=n*n
sum=0
sum1=0
while n!=0:
    r=n%10
    sum=sum*10+r
    n=n//10
sql=sum*sum
while sql!=0:
    r=sql%10
    sum1=sum1*10+r
    sql=sql//10
if sum1==sq:
    print("True")
else:
    print("False")