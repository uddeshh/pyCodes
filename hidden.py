s='board'
new=''
for i in range(len(s)-1):
    new=new+s[i]
    new=new+(chr(abs(ord(s[i])-ord(s[i+1]))+96))
print(new+s[-1])
