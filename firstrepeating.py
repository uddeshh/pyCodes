# l=list(map(int,input().split()))
l=list(input())
temp=[]
flag=0
for i in l:
    if i not in temp:
        temp.append(i)
    else:
        print(i)
        flag=1
        break
if flag==0:
    print('None')
