n=int(input())
c1=0
c2=0
while n>0:
    r=n%10
    if r%2==0:
        c1+=1
    else:
        c2+=1
    n=n//10
if c1>0 and c2>0:
    print("Mixed")
elif c1>0:
    print("Even")
else:
    print("Odd")
        
    