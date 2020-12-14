k,r=map(int,input().split())
i=1
while True:
    t= (i*k-r)%10==0
    u=(i*k)%10==0
    # print(u,t,i)
    i+=1
    if t or u:
        break
print(i-1)
