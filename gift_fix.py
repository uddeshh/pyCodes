t=int(input())
for i in range(t):
    n=int(input())
    C=list(map(int,input().split()))
    O=list(map(int,input().split()))
    tot=0
    for j in range(n):
        tot=tot+max((C[j]-min(C)),(O[j]-min(O)))
    print(tot)
