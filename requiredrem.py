t=int(input())
# for i in range(t):
#     x,y,n=map(int,input().split())
#     if n>=x:
#         print(int((n-y)/x)*x + y)
#     else:
#         print(0)
for i in range(t):
    x,y,n=map(int,input().split())
    if (int((n-y)/x)*x + y)>0:
        print(int((n-y)/x)*x + y)
    else:
        print(0)
