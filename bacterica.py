n=int(input())
c=0
while n>0:
    if n%2==0:
        n=int(n/2)
        # print(n,c)
    else:
        n=int(n/2)
        c+=1
        # print(n,c)
print(c)
