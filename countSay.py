# n=int(input())
# c='1'
# for i in range(1,n+1):
#     for j in range(list(c)):
#         if c[j]==c[j+1]:
#             cnt+=1
#         else:cnt=1
#         print(cnt)

n=list(input())
c=0
for i in range(len(n)+1):
    if n[i]==n[i+1]:
        c+=1
    else:
        c=1
    print(n[i],c)
