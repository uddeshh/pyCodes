n,m=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
# print(p)
if m==n:
    print(abs(p[0]-p[n-1]))
else:
    # print(p[m-1],p[0])
    diff=p[m-1]-p[0]
    # print(diff)
    for i in range(m-n+1):
        puz=[]
        for j in range(i,i+n):
            puz.append(p[j])
        # print(puz)
        newdiff=puz[n-1]-puz[0]
        if newdiff<=diff:
            diff=newdiff
            # print(diff,newdiff)
            continue
        else:
            continue
    print(diff)
