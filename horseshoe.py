c = list(map(int,input().split()))
l=[]
for i in c:
    if i not in l:
        l.append(i)
print(4-len(l))
