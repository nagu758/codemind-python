n=int(input())
largest=1
while n>0:
    r=n%10
    if r>largest:
        largest=r
    n=n//10
print(largest)