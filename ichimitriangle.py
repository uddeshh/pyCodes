# def postri(a,b,c,d):
#     for i in range(b,a-1,-1):
#         for j in range(c,b-1,-1):
#             for k in range(d,c-1,-1):
#                 if i+j>k and j+k>i and k+i>j:
#                     return [i,j,k]
# t=int(input())
# for i in range(t):
#     a,b,c,d=map(int,input().split())
#     res=postri(a,b,c,d)
#     print(*res, sep=' ')
# a,b,c,d=map(int,input().split())
# postri(a,b,c,d)

# def postri(a,b,c,d):
#     i,j,k=a,b,c
#     if i+j>k and j+k>i and i+k>j:
#         print(i,j,k)
#     else:
#
#
# a,b,c,d=map(int,input().split())
# postri(a,b,c,d)

a1,a2,a3,a4=map(int,input().split())
l=list(input())
t=0
for i in l:
    if i=='1':
        t=t+a1
    if i=='2':
        t=t+a2
    if i=='3':
        t=t+a3
    if i=='4':
        t=t+a4
print(t)
