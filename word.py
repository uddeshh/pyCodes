s = input()
word=[]
for i in s:
    word.append(i)
up=[]
lw=[]
for i in word:
    if 65<=ord(i)<=90:
        up.append(word.index(i))
    else:
        lw.append(word.index(i))
if len(up)<=len(lw):
    print(s.lower())
else:
    print(s.upper())
