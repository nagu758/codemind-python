n=int(input())
sum=0
for i in range(1,n):
    r=n%i
    if r==0:
        sum+=i
if sum==n:
    print("True")
else:
    print("False")