n = int(input())
cord_list=[]
al=[]
bl=[]
cl=[]
for i in range(n):
    a,b,c=map(int,input().split())
    al.append(a)
    bl.append(b)
    cl.append(c)
    cord_list.append(a+b+c)
if sum(al)==0 and sum(cl)==0 and sum(bl)==0:
    print('YES')
else:
    print('NO')
# print(sum(al),sum(bl),sum(cl))
