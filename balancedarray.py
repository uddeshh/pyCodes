n=int(input())
for i in range(n):
    test=int(input())
    t=test/2
    if t%2!=0:
        print('NO')
    else:
        print('YES')
        # n=int(input())
        even=[]
        odd=[]
        for j in range(1,test+1):
            if j%2==0:
                even.append(j)
            else:
                odd.append(j)
        # print(even,odd)

        t=odd.pop()
        odd.append(t+int(test/2))
        res=even+odd
        print(*res,sep=" ")
