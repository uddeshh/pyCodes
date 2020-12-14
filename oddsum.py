t=int(input())

for i in range(t):
    c=0
    n=int(input())
    l=list(map(int,input().split()))
    for j in l:
        if j%2==1:
            c=1
    if c==0:
        print('NO')
    else:
        print('YES')
