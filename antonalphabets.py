s=input()
l=[]
for i in s:
    if 122>=ord(i)>=97:
        l.append(i)
print(len(set(l)))
