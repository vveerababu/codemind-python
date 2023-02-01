n=int(input())
for i in range(n):
    n1=int(input())
    a=0
    c=n1
    while True:
        for i in range(2,c//2+1):
            if c%i==0:
                break
        else:
            a=c
            break
        c+=1
    d=n1
    b=0
    while True:
        for i in range(2,d//2+1):
            if d%i==0:
                break
        else:
            b=d
            break
        d-=1
    x=abs(n1-a)
    y=abs(n1-b)
    if x<y:
        print(a)
    else:print(b)