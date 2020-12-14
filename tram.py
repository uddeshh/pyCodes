# n = int(input())
# capacity=[]
# al=[]
# bl=[]
# for i in range(n):
#     a,b = list(map(int,input().split()))
#     al.append(a)
#     bl.append(b)
# al.remove(al[0])
# l=[]
# for i,j in zip(al,bl):
#     l.append(j-i)
#
# l.insert(0,0)
# final=[]
# for i in range(4):
#     final.append(l[i]+bl[i])
# print(max(final))


n = int(input())
ini=0
capacity=[]
for i in range(n):
    a,b = map(int , input().split())
    net = b-a
    cap=net+ini
    capacity.append(cap)
    ini=cap

print(max(capacity))
