t=int(input())
# for i in range(t):
#     n=int(input())
#     p=list(map(int,input().split()))
#     diff=max(p)-min(p)
#     for j in p:
#         for k in p:
#             if abs(j-k)<=diff and p.index(j)!=p.index(k):
#                 ab=[]
#                 ab.append(j)
#                 ab.append(k)
#                 diff=abs(j-k)
#     print(ab, abs(ab[0]-ab[1]))

for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    p.sort()
    ini=0
    diff=[]
    for j in p:
        diff.append(abs(j-ini))
        ini=j
    diff.pop(0)
    print(min(diff))
