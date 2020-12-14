l=list(map(list,input().split()))
# print(l)
# for i in range(len(l[0])):
#     for j in range(1,len(l)):
#         if l[0][i]==l[j][i] and l[j+1]!=None:
#             print(j[i])
i=0
while i<len(l[0]):
    ref=l[0][i]
    c=1
    for j in range(1,len(l)):
        if ref==l[j][i]:
            c+=1
        else:
            break
        if c==len(l):
            print(ref)
    i+=1
