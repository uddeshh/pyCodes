def gcd(n,m):
    if n==0:
        return m
    if m==0:
        return n
    else:
        while n>0 or m>0:
            if n>m:
                n=n-m
            elif m>n:
                m=m-n
            else:
                break
        return n


def gcd_arr(arr):
    # print(arr)
    if len(arr)<=2:
        return gcd(arr[0],arr[1])
    else:
        old=gcd(arr[0],arr[1])
        for i in range(2,len(arr)):
            new=gcd(old, arr[i])
            old=new
        return new


def pass_arr(l,r):
    # print(r)
    final=[]
    for i in r:
        # print(i,int(i[0]),int(i[1]))
        a,b=int(i[0]),int(i[1])
        arr=l[a:b+1]
        ans=gcd_arr(arr)
        final.append(ans)
    return final


l=list(map(int,input().split()))
s=input()
res = [int(i) for i in s if i.isdigit()]
# print(res)
res1=[]
i=0
n=len(res)
while n>0:
    res1.append([res[i],res[i+1]])
    i+=2
    n=n-2

ans=pass_arr(l,res1)
print(*ans,sep=' ')
