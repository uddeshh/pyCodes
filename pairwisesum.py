t=int(input())

for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                if l[i]+l[j]==k:
                    c+=1
                    # print([i,j])
            else:
                pass
    print(int(c/2))
