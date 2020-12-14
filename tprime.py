import math
n = int(input())
l=list(map(int,input().split()))
for i in l:
    sq=pow(i,0.5)

import math
# n = int(input())
l=list(map(int,input().split()))
for i in l:
    sq=math.sqrt(i)
    if sq-math.floor(sq)!=0:
        print('1NO')
    else:
        c=0
        for j in range(2,int(sq)):
            if sq%j==0:
                print('YES')
