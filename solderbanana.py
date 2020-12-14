k,n,w = map(int,input().split())
for i in range(w+1):
    n-=i*k
if n>=0:
    print(0)
else:
    print(abs(n))
