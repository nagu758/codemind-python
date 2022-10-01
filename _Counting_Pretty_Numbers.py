t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=0
    for i in range(a,b+1):
        r=i%10
        if r==2 or r==3 or r==9:
            s+=1
    print(s)