n,m=map(int,input().split())
if n%2==0 and m%2==0:
    print('Malvika')
if n%2!=0 and m%2!=0:
    print('Akshat')
if n%2!=0 and m%2==0:
    if m>n:
        print('Akshat')
    else:
        print('Malvika')
if n%2==0 and m%2!=0:
    if m<n:
        print('Akshat')
    else:
        print('Malvika')
