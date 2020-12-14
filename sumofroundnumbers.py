t=int(input())
for i in range(t):
    n=input()
    op=[]
    c=0
    num= [i for i in n]
    for j in range(len(num)):
        f=int(num[j])*(pow(10,len(num)-j-1))
        if f!=0:
            op.append(str(f))
            c+=1
    res=' '.join(op)
    print(c)
    print(res)
