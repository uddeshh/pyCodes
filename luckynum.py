# n=input()
# if int(n)%4==0 or int(n)%7==0:
#     print('YES')
# else:
#     if '4' in n and '7'in n and '0' not in n and '1'  and '2' not in n and '3' not in n and '5' not in n and '6' not in n and '8' not in n and '9' not in n:
#         print('YES')
#     else:
#         print('NO')
n=int(input())
if n%4==0 or n%7==0 or (n % 44) == 0 or ((n % 47) == 0) or ((n % 74) == 0) or ((n % 444) == 0) or ((n % 447) == 0) or ((n % 474) == 0) or ((n % 477) == 0):
    print('YES')
else:
    print('NO')
