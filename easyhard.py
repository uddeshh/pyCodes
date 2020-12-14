n=input()
r = list(map(int,input().split()))
for i in r:
    if i==0:
        p=0
    else:
        p=i
        break
if p==0:
    print('EASY')
else:
    print('HARD')
