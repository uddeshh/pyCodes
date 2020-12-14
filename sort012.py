n=int(input())
l=list(map(int,input().split()))
zero=l.count(0)
one=l.count(1)
two=l.count(2)
res=[]
num=[zero,one,two]
p=0
for i in num:
    for j in range(i):
        res.append(p)
    p+=1
print(res)
