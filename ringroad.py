n,m= map(int,input().split())
l= list(map(int,input().split()))
ini=0
c=0
e=l[m-1]-1
for i in range(m):
    diff=l[i]-ini
    ini=l[i]
    if diff<0:
        c+=1
ld=c*n
print(ld+e)
