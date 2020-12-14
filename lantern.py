n,l = map(int,input().split())
a=list(map(int,input().split()))
a.sort()
f=a[0]
e=l-a[n-1]
res=max(f,e)
ini=0
for i in a:
    mx=(i-ini)/2
    ini=i
    if mx>res:
        res=mx

print(res)
