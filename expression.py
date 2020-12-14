a=int(input())
b=int(input())
c=int(input())
l=[a,b,c]
if max(a,b,c)==1:
    print(a+b+c)
elif a==1 and b!=1 and c!=1:
    print((a+b)*c)
elif c==1 and b!=1 and a!=1:
    print(a*(b+c))
elif b==1 and a!=1 and c!=1:
    if max(a,b,c)==a:
        print(a*(b+c))
    elif max(a,b,c)==c:
        print((a+b)*c)
elif min(a,b,c)>=2:
    print(a*b*c)
elif l.count(1)==2:
    if max(a,b,c)==b:
        print(a+b+c)
    else:
        print(2*max(a,b,c))
