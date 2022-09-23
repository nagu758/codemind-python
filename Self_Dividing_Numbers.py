n1=int(input())
n2=int(input())
s=0
count=0
for i in range(n1,n2+1):
    s=i
    c=0
    while i:
        r=i%10
        if r==0:
            i=i//10
            continue
        if s%r==0:
            c+=1
        i=i//10
    if len(str(s))==c:
        print(s,end=" ")