n=int(input())
s=list(map(int,input().split()))
mx=s[0]
mn=s[0]
c=0
for i in range(1,n):
    if s[i]>mx:
        mx=s[i]
        c+=1
    elif s[i]<mn:
        mn=s[i]
        c+=1
    else:
        continue
print(c)
