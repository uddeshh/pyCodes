n = int(input())
s=input().lower()
r=[]
if n <26:
    print('NO')
else:
    for i in s:
        if i not in r:
            r.append(i)
    if len(r)==26:
        print('YES')
    else:
        print('NO')
