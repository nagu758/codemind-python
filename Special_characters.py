s = input()
c=[]
for i in s:
    if i.isdigit():
        c.append(i)
k=[]
m=[]
for i in c:
    if int(i)%2==0:
        k.append(i)
    else:
        m.append(i)
g=[]
for i in s:
    if(i in "!@#$%^&*()_-+={[}]:;,>.?/|"):
        g.append(i)
    s1 = len(k)
    s2 = len(m)
    s3 = max(s1,s2)
if(len(g)%2==0):
    for i in range(s3):
        if(i<s1):
            print(k[i],end="")
        if(i<s2):
            print(m[i],end="")
else:
    for i in range(s3):
        if(i<s2):
            print(m[i],end="")
        if(i<s1):
            print(k[i],end="")
                        
        
        