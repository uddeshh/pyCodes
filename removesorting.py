t= int(input())
for i in range(t):
    n=int(input())
    a= list(map(int,input().split()))
    if n==1:
        ini=n
        print('YES')
    else:
        k=0
        a.sort()
        ini=a[0]
        for j in a:
            if abs(ini-j)>1:
                print('NO')
                k=1
                break
            ini=j
        if k==0:
            print('YES')
