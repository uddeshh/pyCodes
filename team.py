
def teams():
    n = int(input())
    total = 0
    for i in range(n):
        ex = input().split()
        l = map(int,ex)
        nl = list(l)
        t = sum(nl)
        if t>=2:
            total += 1
        else: continue
    print(total)

teams()
