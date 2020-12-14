a,b=map(int,input().split())
arr=[1]*(b+1)
arr[0]=0
arr[1]=0
if a>=b: print('INVALID RANGE')
else:
    for i in range(2,int((b+1)**0.5)+1):
        for j in range(i+1,b+1):
            if j%i==0:
                arr[j]=0
    for i in range(a,b+1):
        if arr[i]==1:
            print(i,end=' ')
