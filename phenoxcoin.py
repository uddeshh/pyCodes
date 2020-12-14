# t=int(input())
#
# for i in range(t):
#     n=int(input())
#     if n==2:
#         print(2)
#     else:
#         if (n/2)%2!=0:
#             sum1,tot=0,0
#             for j in range(1,n-2,2):
#                 sum1=sum1+pow(2,j)
#             for j in range(1,n):
#                 tot=tot+pow(2,j)
#             sum2=tot-sum1
#             print(abs(pow(2,n)+sum1-sum2))
#         else:
#             sum1,tot=0,0
#             for j in range(1,n+1,4):
#                 arr=[]
#                 for k in range(j,j+4):
#                     arr.append(k)
#             sum1=sum1+pow(2,arr[0])+pow(2,arr[3])
#             for j in range(1,n+1):
#                 tot=tot+pow(2,j)
#             sum2=tot-sum1
#             print(abs(sum1-sum2))

t=int(input())
for i in range(t):
    n = int(input())
    p=pow(2,(n/2)+1)
    print(int(p)-2)
