n,t = map(int, input().split())
s = input()
sl=[]
for i in s:
    sl.append(i)
# print(sl)
# in_g=[]
# in_b=[]
# for i in range(n):
#     if sl[i]=='B':
#         in_b.append(i)
#     else:
#         in_g.append(i)
# print(in_b,in_g)
#
# for k in range(len(in_g)-1):
#     for j in range(t):
#         sub =in_g[k+1] - in_g[k]
#         print(sub)
#         if  abs(sub)!=1:
#             in_g.insert(k+1,in_b[j])
#         else:
#             break
# print(in_g)
# for i in range(n):
#     print(sl[in_g[i]])
for i in range(n):
        if sl[i]=="B" and sl[i+1]=="G":
            sl[i]='G'
            sl[i+1]='B'
        else:
            break
print(sl)
