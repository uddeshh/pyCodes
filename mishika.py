n=int(input())
cntc,cntm=0,0
for i in range(n):
    m,c=map(int,input().split())
    if m>c:
        cntm+=1
    elif c>m:
        cntc+=1
if cntm>cntc:
    print('Mishka')
elif cntc>cntm:
    print('Chris')
else:
    print('Friendship is magic!^^')
