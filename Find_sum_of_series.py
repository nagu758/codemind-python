n=int(input())
sum=0
for i in range(1,n+1):
    r=1/i
    sum+=r
sum_float='{:.2f}'.format(sum)
print(sum_float)