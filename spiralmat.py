a=[[1,2,399],[4,5,6],[7,8,9],[10,11,12]]
i1=0
mx=[]
mX=0
while i1<len(a[0]):
    i2=0
    while i2<len(a):
        for i in range(3):
            for j in range(3):
                if i-i1==j-i2 and i>i1 and j>i2:
                    tot=0
                    res=[]
                    for k in range(i1,i+1):
                        tot=tot+sum(a[k][i2:j+1])
                    mx.append(tot)
                    if tot>mX:
                        mX=tot
                        for k in range(i1,i+1):
                            print(a[k][i2:j+1])
        i2+=1
    i1+=1
print(mx)
