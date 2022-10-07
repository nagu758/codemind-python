a,b = map(int,input().split())
if a>b:
    high=a
else:
    high=b
value=high
while True:
    if high%a==0 and high%b==0:
        lcm=high
        print(lcm)
        break
    else:
        high=high+value


    
    