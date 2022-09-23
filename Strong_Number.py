n=int(input())
t=n
fact2=1
sum1=0
sum2=0
while n>0:
    r=n%10
    fact2=1
    for i in range(1,r+1):
        fact2=fact2*i
    sum2=sum2+fact2
    n=n//10
if t==sum2:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")