n,m=map(int,input().split())
day=0
while n>0:
    if day%m==0:
        n=n
    else:
        n=n-1
    day+=1
    # print(day,n)
print(day-1)
