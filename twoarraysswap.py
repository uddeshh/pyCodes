t=int(input())

def swapp(a,b):
    mna=min(a)
    mxb=max(b)
    a.remove(mna)
    b.remove(mxb)
    a.append(mxb)
    b.append(mna)
    return a
    return b


for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    inisum=sum(a)
    newsum=sum(a)
    for j in range(k):
        swapp(a,b)
        if sum(a)>inisum:
            inisum=sum(a)
        else:
            break
    print(inisum)
