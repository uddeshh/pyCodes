# # arr=list(map(int,input().split()))
# mat=    [   [1, 0, 1],
#         [1, 1, 1],
#         [1, 1, 1]   ]
# # print(len(mat),len(mat[0]))
# row,coloum=len(mat),len(mat[0])
# print(row,coloum)
# # print(mat.size())
# Zero=[]
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if mat[i][j]==0:
#             Zero.append([i,j])
# # print(Zero)
# for k in Zero:
#     print(k)
#
#     mat[:,k[1]]=[0]*row
#     mat[k[0]][:]=[0]*coloum
#     # for i in range(row):
#     #     mat[i][k[1]]=0
#     # for j in range(coloum):
#     #     mat[k[0]][j]=0
#     # for m in range(len(mat)):
#     #     for n in range(len(mat[0])):
#     #         # print([m,n])
#     #         if n==k[1] or m==k[0]:
#     #             mat[m][n]=0
# print(mat)

l=list(map(int,input().split()))
res=[]
for i in l:
    res.append(list(str(i)))
res.sort(reverse=True)
print(res)
