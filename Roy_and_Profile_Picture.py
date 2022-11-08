n=int(input())
t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a<n or b<n:
        print("UPLOAD ANOTHER")
    elif a==b:
        print("ACCEPTED")
    else:
        print("CROP IT")