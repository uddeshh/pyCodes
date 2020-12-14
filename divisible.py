n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a<=b:
        print(b-a)
    else:
        if a/b==int(a/b):
            print(0)
        else:
            print((int(a/b)+1)*b - a)
