from math import*
m = int(input())
n = int(input())
c = 0
l = [True]*(n+1)
l[0],l[1] = False,False
sq = int(sqrt(n))
for i in range(2,sq+1):
    for j in range(i*i,n+1,i):
        l[j]=False
for i in range(m,n+1):
    if l[i] == True:
        c=c+1
print(c)
