n,m =map(int,input().split())

for i in range(1,n+1):
    row=''
    if i%2!=0:
        for j in range(m):
            row=row+'#'
    else:
        if i%4!=0:
            for j in range(m-1):
                row=row+'.'
            row=row+'#'
        else:
            for j in range(1,m):
                row=row+'.'
            row='#'+row
    print(row)
