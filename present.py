n= input()
l = list(map(int,input().split()))
f=[]
for i in l:
    val=l.index(i)+1
    f.append(str(l.index(val)+1))
op = ' '.join(f)
print(op)
