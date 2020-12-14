n=int(input())
odd=[]
eve=[]
res=[0]*n
k=1
for i in range(n):
    new=[]
    for j in range(1,n+1):
        new.append(k)
        k+=1
    if i%2==0:
        eve.append(new)
    else:
        odd.append(new)
for i in eve:
    print(*i,sep='*')
for i in range(len(odd)):
    print(*odd[(len(odd)-1-i)],sep='*')
