n=int(input())
i=1
while n>0:
    t=int((i*(i+1))/2)
    n=n-t
    i+=1

if n==0:
    print(i-1)
else:
    print(i-2)
