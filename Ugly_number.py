def ugly(n):
    while n>0:
        f=0
        if n%5==0:
            n=n//5
            f=1
        elif n%3==0:
            n=n//3
            f=1
        elif n%2==0:
            n=n//2
            f=1
        if f==0 or n==1:
            break
    if n==1:
        print('Ugly Number')
    else:
        print('Not Ugly Number')
n=int(input())
ugly(n)