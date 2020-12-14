n = int(input())
cnt=0
hl=[]
gl=[]
for i in range(n):
    h,g=map(int,input().split())
    hl.append(h)
    gl.append(g)

for i in hl:
    for j in gl:
        if i==j:
            cnt+=1
print(cnt)
