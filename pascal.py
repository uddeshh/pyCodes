# import math
A=int(input())
# first=[1]
# second=[1,1]
# res=[first,second]
# for i in range(3,n+1):
#     arr=[0]*i
#     arr[0]=1
#     if i%2==0:
#         for j in range(1,int(i/2)):
#             arr[j]=second[j]+second[j-1]
#             arr=arr[:j+1:1]+arr[j::-1]
#         second=arr
#     else:
#         for j in range(1,int(i/2)+1):
#             arr[j]=second[j]+second[j-1]
#             arr=arr[:j:1]+arr[j::-1]
#         second=arr
#     res.append(arr)
# if n==0:
#     print(0)
# elif n==1:
#     print([[1]])
# else:
#     print(res)

l=[]
for i in range(A):
    for j in range(i+1):
        if j==0 or j==i:
            l.append(1)
        else:
            l.append(l[i-1][j]+l[i-1][j-1])
        print(l)
