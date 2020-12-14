n=int(input())
a=list(map(int,input().split()))
# print(a)
l=list(set(a))
acnt=[]
for i in l:
    acnt.append([a.count(i),i])
    # print(acnt)
m=max(acnt)[1]
# print(m)
a.remove(m)
l=[]
for j in a:
    if j!=(m-1) and j!=(m+1) :
        l.append(j)
print(m+sum(l))
