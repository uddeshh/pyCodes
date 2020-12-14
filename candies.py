# t=int(input())
# for i in range(t):
#     n=int(input())
#     # for j in range(1,int(n/2)+1):
#     j=1
#     while j<n/2+1:
#         tot=0
#         # for k in range(int(n/2)+1):
#         k=0
#         while k<n/2+1:
#             tot=tot+(2**k)*j
#             if tot==n:
#                 print(j)
#                 break
#             if tot>n:
#                 break
#             k+=1
#         if tot==n:
#             break
#         j+=1

t=int(input())
for i in range(t):
    n=int(input())
    p=3
    while n%p>0:
        p=1+2*p
    print(int(n/p))
