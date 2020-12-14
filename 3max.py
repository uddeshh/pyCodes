l=list(map(int,input().split()))
# f=0
# s=0
# t=0
# for i in l:
#     if i>f:
#         t=s
#         s=f
#         f=i
#     elif i>s:
#         t=s
#         s=i
#     else:
#         t=i
# print(f,s,t)


n=len(l)
# piv=l[]
# for i in range(n)
left=l[:int(n/2)]
right=l[int(n/2):]
for i in range(len(left)):
    pos=i
    cursor=left[pos]
    # flag=0
    while pos>0 and left[pos-1]>cursor:
        left[pos]=left[pos-1]
        pos=pos-1
        # flag=1
    left[pos]=cursor
    # if flag==0:
        # break
print(left)
for i in range(len(right)):
    pos=i
    # flag=0
    cursor=right[pos]
    while pos>0 and right[pos-1]>cursor:
        right[pos]=right[pos-1]
        pos=pos-1
        # flag=1
    right[pos]=cursor
    # if flag==0:
    #     break
print(right)

for i in range(3):
    # print('hi')
    if left[len(left)-1]>right[len(right)-1]:
        print(left[len(left)-1])
        left.pop()
    else:
        print(right[len(right)-1])
        right.pop()
