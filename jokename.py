a = input()
b = input()
ab = input()
f=a+b
if len(f)!=len(ab):
    print('NO')
else:
    for i in range(len(ab)):
        if f.count(f[i])==ab.count(f[i]):
            op=1
        else:
            op=0
            break
    if op!=1:
        print('NO')
    else:
        print('YES')
