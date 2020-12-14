n = int(input())
l=list(map(int ,input().split()))
p1,p2,j,k=0,0,0,0
for i in range(n):
    if l[i]%2==0:
        j+=1
        p1=i
    if l[i]%2==1:
        k+=1
        p2=i
if j>k:
    print(p2+1)
else:
    print(p1+1)
