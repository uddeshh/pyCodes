n=int(input())
l=[]
for i in range(1,n+1):
    # if i==1:
    #     l.append()
    if i%2==0:
        l.append('I love ')
    else:
        l.append('I hate ')
res='that '.join(l) + 'it'
print(res)
