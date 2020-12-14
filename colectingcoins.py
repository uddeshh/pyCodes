t=int(input())
for i in range(t):
    c= list(map(int,input().split()))
    if sum(c)%3==0 and max(c[:len(c)-1])<=int(sum(c)/3):
        print('YES')
    else:
        print('NO')
