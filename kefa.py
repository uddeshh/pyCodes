n = int(input())
e = list(map(int,input().split()))
i=0
new=0
while i<n:
    temp,c=0,0
    for j in range(i,n):
        if e[j]>=temp:
            c+=1
            temp=e[j]
            i+=1
        else:
            i=j
            break
    if new<c:
        new=c
print(new)
