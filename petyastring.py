w1 = input().lower()
l1=[]
for i in w1:
    l1.append(i)
w2 = input().lower()
l2=[]
for i in w2:
    l2.append(i)
res=[]
if len(w1)==len(w2):
    for i in range(len(w1)):
        if l1[i]>l2[i]:
            res.append(1)
            break
        elif l1[i]<l2[i]:
            res.append(-1)
            break
        else:
            res.append(0)
print(sum(res))
