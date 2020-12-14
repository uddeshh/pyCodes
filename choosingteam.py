n,k=map(int,input().split())
sc=list(map(int,input().split()))
sc.sort()
c=0
i=0
while i<=n-3:
    # print(f'index {i}')
    tot=[]
    for j in range(i,i+3):
        tot.append(sc[j])
    mx=max(tot)
    # print(tot)
    # print(f'max {mx}')/
#     if mx>k:
#         print(0)
#         i+=1
#     else:
#         if mx+k<=5:
#             print(f'diff {k-mx}')
#             c+=1
#             print(f'count {c}')
#             i+=3
#             # break
#         else:
#             i+=1
#     print(f'index2 {i}')
# print(c)


    if mx+k<=5:
        # print(f'diff {k-mx}')
        c+=1
        # print(f'count {c}')
        i+=3
            # break
    else:
        i+=1
    # print(f'index2 {i}')
print(c)
