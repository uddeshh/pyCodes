n=int(input())
# c=0
# for i in range(1,n):
#     for j in range(1,n):
#         if (i*j)+i==n:
#             c+=1
#             break
# print(c)
c=0
for i in range(1,int(n/2)+1):
    if n%i==0:
        c+=1
print(c)
# i=1
# while i<n:
#     j=1
#     while j<n:
#         if (n-i)%i==0:
#             c+=1
#             print(i,j,'as')
#             break
#         j+=1
#         print(i,j)
#     i+=1
# print(c)
