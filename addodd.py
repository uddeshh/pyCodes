t=int(input())

for i in range(t):
    a,b=map(int,input().split())

    if a==b:
        print(0)
    elif a>b:
        if a%2==0 and b%2==0:
            print(1)
        elif a%2!=0 and b%2!=0:
            print(1)
        elif a%2==0 and b%2!=0:
            print(2)
        elif a%2!=0 and b%2==0:
            print(2)
    elif a<b:
        if a%2==0 and b%2==0:
            print(2)
        elif a%2!=0 and b%2!=0:
            print(2)
        elif a%2==0 and b%2!=0:
            print(1)
        elif a%2!=0 and b%2==0:
            print(1)
