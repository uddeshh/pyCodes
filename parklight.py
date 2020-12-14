t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if (m*n)%2==0:
        # print('hi1')
        print(int((m*n)/2))
    else:
        # print('hi2')
        print(int(((n*m)+1)/2))
