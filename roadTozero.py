def toZero(x,y,a,b):
    cost=0
    if x>=y:
        cost=min(y*2*a,y*b)+(x-y)*a
    else:
        cost=min(x*2*a,y*b)+(-x+y)*a
    return cost

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    print(toZero(x,y,a,b))
