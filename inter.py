def interleaving(a,b,c):
    i,j,k=0,0,0
    res=True
    while i<len(c):
        if j<len(a) and a[j]==c[i] :
            i+=1
            j+=1
            # print(i,j,'a')
        elif k<len(b)and b[k]==c[i] :
            i+=1
            k+=1
            # print(i,k,'b')
        else:
            res=False
            break
    return res
print(interleaving('uddesh','chouhan','choududhesahn'))
