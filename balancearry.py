A=list(map(int,input().split()))
# n=len(A)
# eveSum,oddSum=0,0
# for i in range(n):
#     if i%2==0:
#         eveSum=eveSum+A[i]
#     else:
#         oddSum=oddSum+A[i]
# print(oddSum,eveSum)
# if oddSum==eveSum:
#     # return 0
#     print(0)
# else:
#     c=0
#     for i in range(n):
#         if i%2==0:
#             if eveSum-A[i]==oddSum:
#                 c+=1
#         else:
#             if oddSum-A[i]==eveSum:
#                 c+=1
#     # return c
#     print(c)

# x=A.pop(2)
# print(A,x)
# A.pop(2)
# print(A)


n=len(A)
if n==0 or n==1:
    print(0)
else:
    c=0
    for i in range(n):
        x=A.pop(i)
        print(A)
        os,es=0,0
        for j in range(len(A)):
            if j%2==0:
                es=es+A[j]
            else:
                os=os+A[j]
        print(os,es)
        if os==es:
            c+=1
        A.insert(i,x)
    print(c)
