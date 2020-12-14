n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
f=list(map(int,input().split()))
for i in s:
    if s.count(i)!=t.count(i):
        print(i)
        break
for i in t:
    if t.count(i)!=f.count(i):
        print(i)
        break
