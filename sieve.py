n=int(input())
arr=[1]*(n+1)
# print(arr)

for i in range(2,int(n**(0.5))+1):
    if arr[i]==1:
        for j in range(i+1,n):
            # print(i,j)
            if j%i==0:
                arr[j]=0
print(arr.count(1)-2)
