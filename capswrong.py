p = input()
w=[]
for i in p:
    w.append(i)
for i in range(len(w)):
    if 90>=ord(w[0])>=65:
        for j in range(i,len(w)):
            if 90>=ord(w[j])>=65:
                w[j]=chr(ord(w[j])+32)
            else:
                continue
    elif 122>=ord(w[0])>=97:
        w[0]=chr(ord(w[0])-32)
        for k in range(i,len(w)):
            if 90>=ord(w[k])>=65:
                w[k]=chr(ord(w[k])+32)
            else:
                continue
final=''.join(w)
print(final)
