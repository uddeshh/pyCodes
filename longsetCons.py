t=int(input())

for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    i=0
    f=0
    e=1
    while i<=n:
        print(l[f:e])
        i=i+max(l[f:e])
        f=i-1
        e=l[i-1]
