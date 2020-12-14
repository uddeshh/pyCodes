n=int(input())
pile=list(map(int,input().split()))
t=int(input())
worm=list(map(int,input().split()))
arr=[]
ini=0
for i in pile:
    arr.append([ini,ini+i])
    ini=ini+i
for i in range(t):
    for j in range(n):
        if worm[i]>arr[j][0] and worm[i]<=arr[j][1]:
            print(j+1)
