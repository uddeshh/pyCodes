n=int(input())
l=list(map(int,input().split()))

for i in l:
    if i>=0:
        ini=l.index(i)
        break
for i in range(ini,len(l)):
    for j in range(i,len(l)):
        if l[j]<0:
            l[ini],l[j]=l[j],l[ini]
            ini=j
            break
print(l)
