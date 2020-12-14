import math
n,m,a= map(int,input().split())
# sr,sc=0,0
# for i in range(n+1):
#     if sr < n:
#         sr+=a
#     else:
#         break
# for i in range(m+1):
#     if sc < m:
#         sc+=a
#     else:
#         break
# print(int(sr/a)*int(sc/a))
i=math.ceil(n/a)
j=math.ceil(m/a)
print(int(j)*int(i))
