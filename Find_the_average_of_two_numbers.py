a=list(map(int,input().split()))
a.sort()
avg=(a[0]+a[1])/2
res="{:.4f}".format(avg)
print(res)