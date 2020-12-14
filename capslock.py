p = input()
w=[]
for i in p:
    w.append(i)
nw=[]
l=len(w)

if 122>=ord(w[0])>=97:
    for i in range(1,l):
        if 90>=ord(w[i])>=65:
            nw.append(w[i])

    if len(nw)==len(w)-1:
        w[0]=chr(ord(w[0])-32)
        for j in range(1,l):
            w[j]=chr(ord(w[j])+32)

elif 90>=ord(w[0])>=65:
    for i in range(l):
        if 90>=ord(w[i])>=65:
            nw.append(w[i])

    if len(nw)==len(w):
        for j in range(l):
            w[j]=chr(ord(w[j])+32)

final=''.join(w)
print(final)
