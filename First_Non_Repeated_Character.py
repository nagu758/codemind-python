x = int(input())
for i in range(x):
    n = int(input())
    a = input()
    m = 0
    for j in range(n):
        c = 0
        for k in range(n):
            if(a[j]==a[k] and j!=k):
                c=1
                break
        if(c==0):
            print(a[j],end="
")
            m=1
            break
    if(m==0):
        print("-1",end="
")
                