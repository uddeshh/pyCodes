n=int(input())
res=[]
if n%2==0:
    print(int(n/2))
    for i in range(int(n/2)):
        res.append(2)
else:
    print(int(n/2))
    for j in range(int(n/2)-1):
        res.append(2)
    res.append(3)

print(*res,sep=' ')
