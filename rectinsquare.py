t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a<b:
        if 2*a>b:
            area=(a+a)**2
        else:
            area=b*b
    else:
        if 2*b>a:
            area=(b+b)**2
        else:
            area=a*a
    print(area)
