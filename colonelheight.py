n = int(input())
h = list(map(int,input().split()))
mn,mx=[],[]
if min(h)!=max(h):
    for i in range(n):
        if h[i]==min(h):
            mn.append(i)
        elif h[i]==max(h):
            mx.append(i)
        else:
            continue
    cor_min=max(mn)+1
    cor_max=min(mx)+1
    res=(n-cor_min) + (cor_max-1)
    if cor_max>cor_min:
        print(res-1)
    else:
        print(res)
else:
    print(0)
