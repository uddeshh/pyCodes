m,n = map(int,input().split())
t = 0
for d in range(m*n):
    if (m*n)%2==0:
        if m*n > 2*d:
            t += 1
            final = t
        else:
            break
    else:
        if m*n > 2*d:
            t += 1
            final = t-1
        else:
            break
print(final)
