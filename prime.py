# A=int(input())
# arr=[1]*A
# for i in range(2,A):
#     for j in range(i+1,A):
#         if j%i==0:
#             arr[j]=0
# print(arr)
# i=2
# while i<A:
#     if arr[i]==1 and arr[A-i]==1 :
#         print(i,A-i)
#     i+=1
def fact(A):
    while A>1:
        return A*fact(A-1)
print(fact(int(input())))
