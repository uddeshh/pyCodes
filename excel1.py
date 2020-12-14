A=list(input().upper())
A=A[::-1]
tot=0
for i in range(len(A)):
    print((ord(A[i])-64)*(i+1)+24*i)
    # tot=tot+((ord(A[i])-64)*(i+1)+24*i)
# print(tot)
