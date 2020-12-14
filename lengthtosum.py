# m,s=map(int,input().split())
# a=s
# b=s
# if s==0:
#     print(-1,-1)
# else:
#     if m==1:
#         x,y=s,s
#     else:
#         mx=[]
#         for i in range(m):
#             if s>9:
#                 mx.append(9)
#                 s=s-9
#             else:
#                 if s>=1:
#                     mx.append(s)
#                     s=0
#                 else:
#                     mx.append(0)
#         temp=mx[::-1]
#         if temp==mx:
#             mn=mx
#         else:
#             if m==2:
#                 mn=mx[::-1]
#             else:
#                 mn=[]
#                 for j in range(m):
#                     if a>9:
#                         mn.append(9)
#                         a-=9
#                     else:
#                         if a>0:
#                             mn.append(a)
#                             a=0
#                         else:
#                             mn.append(0)
#                 if mn[j]==0:
#                     ind=mn.index(0)
#                     mn[ind-1]=mn[ind-1]-1
#                     mn[j]=1
#                 mn=mn[::-1]
#             x,y,='',''
#             for l in mn:
#                 x=x+str(l)
#             for m in mx:
#                 y=y+str(m)
#     if b==1 and m==2:
#         print(y,y)
#     else:
#         print(x,y)
m,s=map(int,input().split())
a=s
# print(s/m)
if s==0 and m!=1  or s/m>9:
    print(-1,-1)
else:
    if m==1:
        if s>9:
            print(-1,-1)
        else:
            x,y=s,s
            print(x,y)
    else:
        mx=[]
        for i in range(m):
            if s>9:
                mx.append(9)
                s=s-9
            else:
                if s>=1:
                    mx.append(s)
                    s=0
                else:
                    mx.append(0)
        if a==1 and m==2:
             mn=mx
        else:
            temp=mx[::-1]
            if temp==mx:
                mn=mx
            else:
                if m==2 and s>9:
                    mn=mx[::-1]
                else:
                    mn=[]
                    for j in range(m):
                        if a>9:
                            mn.append(9)
                            a-=9
                        else:
                            if a>0:
                                mn.append(a)
                                a=0
                            else:
                                mn.append(0)
                    if mn[j]==0:
                        ind=mn.index(0)
                        mn[ind-1]=mn[ind-1]-1
                        mn[j]=1
                    mn=mn[::-1]
        x,y,='',''
        for l in mn:
            x=x+str(l)
        for m in mx:
            y=y+str(m)
        print(x,y)
