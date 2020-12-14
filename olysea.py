n,t= map(int, input().split())
if t<=9:
    print(t*10**(n-1))
else:
    if n==1:
        print(-1)
    else:
        print(t*10**(n-2))
