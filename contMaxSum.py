# l=list(map(int,input().split()))
# temp=[]
# total=[]
# tot=0
# for i in l:
#     if i >0:
#         temp.append(i)
#         tot+=i
#         total.append([tot,temp])
#     else:
#         temp=[]
#         tot=0
# print(max(total)[1])



#code
t=int(input())

for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    c=0
    i=0
    mx=0
    while i+1<n :
        if l[i+1]-l[i]<1:
            c=c+1
        else:
            c=0
        if mx<c:
            mx=c
        i+=1
    print(mx)
