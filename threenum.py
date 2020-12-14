l=list(map(int,input().split()))
l.sort()
mx=max(l)
l.pop()
res=[]
for i in l:
    diff=mx-i
    res.append(str(diff))
res1=' '.join(res)
print(res1)
