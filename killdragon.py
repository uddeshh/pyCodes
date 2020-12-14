s,n = map(int,input().split())
l=[]
for i in range(n):
    c=0
    [x,y]= map(int,input().split())
    l.append([x,y])
l.sort()
# print(l)
for i in range(n):
    if s>l[i][0]:
        s=s+l[i][1]
        c=0
    else:
        print('NO')
        c=1
        break
if c==0:
    print('YES')
