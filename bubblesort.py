l = list(map(int , input().split()))
lg=len(l)
for i in range(lg):
    for j in range(lg):
        n=j+1
        if n<lg:
            if l[j]>l[n]:
                l[j],l[n]=l[n],l[j]
print(l)
