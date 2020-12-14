n=int(input())
ini=[1 for i in range(n)]

# for i in range(n):
#     new=[]
#     k=0
#     # print(type(k),type(ini[0]))
#     for j in ini:
#         nsm=j+k
#         k=nsm
#         new.append(nsm)
#     ini=new
#     print(new)
if n==1:
    print(1)
else:
    for i in range(n-1):
        new=[]
        k=0
        for j in range(n):
            nsm=ini[j]+k
            k=nsm
            new.append(nsm)
        ini=new
    print(max(new))
