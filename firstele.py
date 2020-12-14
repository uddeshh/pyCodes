# A=list(map(int,input().split()))
# poz=[]
# for i in A:
#     if i not in poz and i>0:
#         poz.append(i)
#
# if len(poz)==0:
#     print(1)
# else:
#     arr=[0]*(max(poz)+1)
#     for i in poz:
#         arr[i]=i
#     print(arr)
#     for i in range(len(arr)):
#         if i!=arr[i]:
#             print(i)
#             break
#     else:
#         print(i+1)
# rep,miss=0,0
# for i in range(1,max(A)+1):
#     if A.count(i)>1:
#         rep=i
#     if A.count(i)==0:
#         miss=i
# print(rep,miss)

# for i in range(max(A)):
#     if A[i] in A[i+1:]:
#         # print(A[i],A[i+1:])
#         rep=A[i]
#         print(rep,'rep')
#     if i not in A and i!=0:
#         miss=i
#         print(miss,'miss')
# print(rep,miss)
# n=max(A)
# ActSum=n*(n+1)/2
# ArrSum=sum(A)
# SqActSum=n*(n+1)*(2*n+1)/6
# SqArrSum=0
# for i in A:
#     SqArrSum=SqArrSum+i*i
#
# # ActSum=ArrSum-rep+miss
# # SqActSum=SqArrSum-rep**2+miss**2
# print(ActSum,ArrSum)
# print(ActSum-ArrSum)
# print(SqActSum,SqArrSum)
# print(SqActSum-SqArrSum)
