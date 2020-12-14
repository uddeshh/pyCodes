n = int(input())
a,b=3,n-3
ans=[]
while a<=b:
    a+=1
    b-=1
    for i in range(2,a):
        if a%i==0:
            ans=a
            # print(ans)
            for j in range(2,b):
                if b%j==0:
                    ans=ans+b
                    # print(ans)
                    break
    if ans==n:
        print(a,b)
        break
