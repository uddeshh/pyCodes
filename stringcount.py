s=input()
l=[]

for i in set(s):
    c=0
    for j in s:
        if i==j:
            c+=1
    if c>1:
        print(i,c)
