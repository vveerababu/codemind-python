n=int(input())
s=1
for i in range(2,n):
    if n%i==0:
        s=s+i
if s>n:
    print(True)
else:
    print(False)