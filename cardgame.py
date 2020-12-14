card= list(input())
l=list(input().split())
for i in l:
    # print(card[0],card[1],i)
    f=0
    if card[0] in i or card[1] in i:
        print('YES')
        f=1
        break
if f==0: print('NO')
