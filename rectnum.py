# A=int(input())
# arr=[0]*A
# arr[0]=([A]*(2*A-1))
# for i in range(1,A):
#     x=arr[i-1]
#     for j in range(i,(2*A-1)-i):
#         x[j]=x[j]-1
#     arr[i]=x
#     print(x)
# arr=[]
# X=[A]*A
# arr.append(X+X[-2::-1])
# for i in range(A-1):
#     for j in range(i+1,A):
#         X[j]=X[j]-1
#     arr.append(X+X[-2::-1])
# print(arr+arr[-2::-1])

def maXX(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if A[i]<=A[j]:
                print(j-i)
A=list(map(int,input().split()))
maXX(A)
