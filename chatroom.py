word = input()
l=len(word)
if l<=5:
    print('NO')
else:
    for i in range(l):
        if i=='h':
            for j in range(i,l):
                if j == 'e':
                    for k in range(j,l):
                        if k=='l':
                            for m in range(k,l):
                                if k=='l':
                                    for n in range(m,l):
                                        if k=='o':
                                            print('YES')
                                        else:
                                            print('NO')
                                else:
                                    print('NO')
                        else:
                            print('NO')
                else:
                    print('NO')
        else:
            print('NO')



















# import re
# text=input().lower().strip()
# x = re.search("[h]+([a-z]+|)[e]+([a-z]+|)[l]+([a-z]+|)[l]+([a-z]+|)[o]+", text)
# if x == None:
# 	print("NO")
# else:
# 	print("YES")
