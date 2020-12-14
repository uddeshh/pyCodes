w = input().lower()
t = [i for i in w ]
l=[]
for i in t:
    if i=='a' or i=='e' or i=='i'or i=='o' or i=='u' or i=='y':
        continue
    else:
        l.append(i)

s = '.' + '.'.join(l)
print(s)
