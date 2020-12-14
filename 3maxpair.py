t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    arr=[x,y,z]
    if x==y==z:
        print('YES')
        print(x,y,z)
    elif x==y>z or x==z>y or y==z>x:
        print('YES')
        print(max(arr),min(arr),1)
    else:
        print('NO')
