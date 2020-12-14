A=int(input())
# # chr(int(n)+64)
# s=''
# while n>=1:
#     s=s+chr(n%26+int(n/26)+64)
#     n=n//26
#     # print(n)
# print(s)
base_num = ""
while A>0:
    dig =A%26
    if A%26==0:
        base_num += 'z'
    else:
        base_num += chr(dig+64)
    A=int(A/26)
    base_num = base_num[::-1]
print(base_num)
