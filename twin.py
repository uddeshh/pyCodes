n= int(input())
c = list(map(int , input().split()))
if len(c)==n:
    i=0
    ma_s=0
    while i<=n:
        ma_s += max(c)
        c.remove(max(c))
        l_sum = sum(c)
        i+=1
        if ma_s>l_sum:
            print(i)
            break
        else:
            continue
