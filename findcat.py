s=input()
c=0
for i in range(len(s)):
    if s[i] =='c' and s[i:i+3]=='cat':
        c+=1
d=0
for i in range(len(s)):
    if s[i] =='h' and s[i:i+3]=='hat':
        d+=1
if c==d:
    print('YES')
else:
    print('NO')
