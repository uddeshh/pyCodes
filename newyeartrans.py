n,t=map(int,input().split())
a=list(map(int,input().split()))
cell=[a[i]+i+1 for i in range(n-1)]
# print(cell)
if t in cell or t==1:
    print('YES')
elif min(cell)>t:
    print('NO')
else:
    print('NO')
