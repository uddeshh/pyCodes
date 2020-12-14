t=int(input())
for i in range(t):
    n=int(input())
    tot=n
    while n>0:
        if n<9:
            tot=tot+n
        else:
            rem=n%10
            tot=tot+int(n/10)
            n=int(n/10)+rem
    print(tot)
