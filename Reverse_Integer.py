n=int(input())
if n<0:
    n=n*(-1)
    n=str(n)[::-1]
    n=int(n)
    print((-1)*n)
else:
    print(int(str(n)[::-1]))

    