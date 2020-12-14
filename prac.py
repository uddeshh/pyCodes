n=int(input())
even=[]
odd=[]
for i in range(1,n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even,odd)
t=odd.pop()
odd.append(t+int(n/2))
sum(odd)
print(even,odd)
