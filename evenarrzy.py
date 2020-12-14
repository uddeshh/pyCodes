t = int(input())

for i in range(t):
    n=int(input())
    l = list(map(int,input().split()))
    rest=[]
    for j in range(n):
        if j%2!=l[j]%2:
            rest.append(j)
    o,e=0,0
    for k in rest:
        if k%2==0:
            e+=1
        else:
            o+=1
    if o==e:
        print(int(len(rest)/2))
    else:
        print(-1)
