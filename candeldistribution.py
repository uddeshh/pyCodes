import math
n=int(input())
for i in range(n):
    t=int(input())
    if t%2==0:
        print(t-math.ceil((t+1)/2))
    else:
        print(t-math.ceil(t/2))
