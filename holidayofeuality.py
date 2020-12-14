n=int(input())
bur=list(map(int,input().split()))
tot=0
for i in bur:
    tot=tot+(max(bur)-i)
print(tot)
