p= input()
one = p.split('0')
zero = p.split('1')
one_len=[]
zero_len=[]
for i in one:
    one_len.append(len(i))
for j in zero:
    zero_len.append(len(j))
if max(max(one_len),max(zero_len))>=7:
    print('YES')
else:
    print('NO')
