n,k = map(int , input().split())
l = list(map(int , input().split()))
c= 0
for i in l:
    if i>=l[k-1] and i>0:
        c+=1
    else:
        break
print(c)
