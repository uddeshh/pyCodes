first=list(map(int,input().split()))
second=list(map(int,input().split()))
third=list(map(int,input().split()))

for i in first:
    if i in second and i in third:
        print(i)
