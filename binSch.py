arr=list(map(int,input().split()))
arr.sort()
X=int(input())
old=0
while True:
    n=len(arr)
    if n%2==0:
        if arr[int(n/2)]==X:
            print(int(n/2)+old)
            break
        elif arr[int(n/2)]<X:
            arr=arr[int(n/2):]
            old=old+int(n/2)
        else:
            arr=arr[:int(n/2)]
            old=old
    else:
        if arr[int(n/2)]==X:
            print(int(n/2)+old)
            break
        elif arr[int(n/2)]<X:
            arr=arr[int(n/2):]
            old=old+int(n/2)
        else:
            arr=arr[:int(n/2)]
            old=old
