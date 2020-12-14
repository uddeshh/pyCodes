t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    res=[]
    for j in p:
        if j not in res:
            res.append(j)
    print(*res, sep=' ')
