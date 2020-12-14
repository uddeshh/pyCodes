n=int(input())
l=list(map(int,input().split()))
res=0
min=0
for i in l:
    res=res+i
    if res<0:
        if res<min:
            min=res
print(abs(min))
