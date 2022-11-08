s = input()
l = 0
for i in s:
    if i.isdigit():
        l+=int(i)
print(l)