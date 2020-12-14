n,k=map(int,input().split())
if k>n*n or k==0:
    print(0)
else:
    # c=0
    # for i in range(1,n+1):
    #     res=[]
    #     for j in range(1,n+1):
    #         # if i*j==k:
    #         #     c+=1
    #         res.append(i*j)
    #     print(res)
    # # print(c)
    c=0
    for i in range(1,n+1):
        if k%i==0 and k/i<=n:
            c+=1
    print(c)
