import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
res="{:.2f}".format(area)
print(res)