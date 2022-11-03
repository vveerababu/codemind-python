n=int(input())
x=n*n
m=0
while x>0:
    r=x%10
    m+=r
    x=x//10
if m==n:
    print('Neon Number')
else:
    print('Not Neon Number')