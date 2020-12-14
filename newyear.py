n,k=map(int,input().split())
t=240-k
i=0
c=0
for i in range(n+1):
    if t>=5*i:
        t=t-(5*i)
        c+=1
        # print(t)
    else:
        break
print(c-1)
