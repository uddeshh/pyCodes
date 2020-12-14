n= int(input())
l=list(map(int,input().split()))
m= int(input())
p=list(map(int,input().split()))
# a,b=[],[]
# for i in range(n):
#     for j in range(m):
#         if abs(l[i]-p[j])<=1:
#             # print(l[i],p[j])
#             a.append((l[i],p[j]))
#             # b.append()
# b=list(set(a))
# # print(b,b.count(1))
# x,y=[],[]
# for i in b:
#     x.append(i[0])
#     y.append(i[1])

a,b=[],[]
for i in l:
    for j in p:
        if abs(i-j)<=1:
            a.append(i)
            b.append(j)

t=0
for i in list(set(a)):
    if l.count(i) <a.count(i):
        t=t+l.count(i)
    else:
        t=t+a.count(i)
print(t)
t=0
for i in list(set(b)):
    if p.count(i) <b.count(i):
        t=t+p.count(i)
    else:
        t=t+b.count(i)
print(t)
