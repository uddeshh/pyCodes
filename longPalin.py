s=input()
n=len(s)
for i in range(n):
    for j in range(n-1,i,-1):
        if s[i:j]==s[j:i:-1]:
            print(s[i:j+1])

# t=int(input())
# for i in range(t):
#     s=input()
#     n=len(s)
#     res=[]
#     for i in range(n):
#         j=1
#         while j<n+1:
#             res.append(s[i:j])
#             j+=1
#     print(res)

# t=int(input())
#
# for i in range(t):
#     ip=input()
#     s=list(ip)
#     n=len(s)
#     res=[]
#     for i in range(n):
#         for j in range(n):
#             s[i],s[j]=s[j],s[i]
#             new=''.join(s)
#             res.append(new)
#         # res.append(ip[::-1])
#     print(set(res))
