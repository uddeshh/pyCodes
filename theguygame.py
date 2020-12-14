n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
r=[]
for i in x:
    y.append(i)
for j in y:
    if j not in r and j!=0:
        r.append(j)
if len(r)==n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
