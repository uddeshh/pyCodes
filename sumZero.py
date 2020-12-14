l=list(map(int,input().split()))

l.sort()
j,k=0,len(l)-1
for i in range(int(len(l)/2)):
    tot=l[j]+l[k]
    if tot<0:
        j+=1
        # print(tot,i,j,1)
    elif tot>0:
        k-=1
        # print(tot,i,j,2)
    elif tot==0:
        print("YES")
        break
if j==0 or k==len(l)-1:
    print('NO')
