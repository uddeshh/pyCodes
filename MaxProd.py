t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    arr=[]
    prod=1
    for i in l:
        if i>0:
            prod=prod*i
            arr.append(prod)
        else:
            prod=1
    print(max(arr))
