n = input()
sc = input()
l=[]
for i in sc:
    l.append(i)
# cnt=0
# for i in range(len(l)):
#     key=l[i]
#     if key==l[i]:
#         cnt+=1
#     else:
#         pass
# print(cnt)
c=0
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]==l[j] and j-i==1:
            c+=1
print(c)
