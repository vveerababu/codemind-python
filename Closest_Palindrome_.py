n=int(input())
a=n
c=0
while(True):
    a+=1
    rev=int(str(a)[::-1])
    if a==rev:
        c=a
        break
    else:continue
b=n
d=0
while(True):
    b-=1
    rev=int(str(b)[::-1])
    if b==rev:
        d=b
        break
    else:continue
x=abs(n-c)
y=abs(n-d)
if x!=y:
    print(min(d,c))
else:print(d,c)