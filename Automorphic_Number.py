n=int(input())
a=str(n)
n1=n**2
b=str(n1)
if b.endswith(a):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')