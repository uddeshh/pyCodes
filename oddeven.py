n,k=map(int,input().split())
# odd=[]
# even=[]
# for i in range(1,n+1):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# res=odd+even
# print(res[k-1])

#############################################################################
# if n%2==0:
#     if k <= n/2:
#         c=0
#         for i in range(1,n+1,2):
#             c+=1
#             if c==k:
#                 print(i)
#                 break
#             else:
#                 continue
#     else:
#         c=n/2
#         for i in range(2,n+1,2):
#             c+=1
#             if c==k:
#                 print(i)
#                 break
#             else:
#                 continue
# else:
#     if k <= int((n/2))+1:
#         c=0
#         for i in range(1,n+1,2):
#             c+=1
#             if c==k:
#                 print(i)
#                 break
#             else:
#                 continue
#     else:
#         c=int(n/2)+1
#         for i in range(2,n+1,2):
#             c+=1
#             if c==k:
#                 print(i)
#                 break
#             else:
#                 continue
########################################################################33
if k<=(n+1)/2:
    print((k*2)-1)
else:
    print(int((k-int((n+1)/2))*2))
