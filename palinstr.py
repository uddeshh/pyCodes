A=input()
strr=[]
for i in A.lower():
    if ord(i)<=122 and ord(i)>=97:
        strr.append(i)
print(strr)
