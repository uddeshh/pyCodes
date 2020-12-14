n,m=map(int,input().split())
c=0
for i in range(n):
    l=list(input().split())
    c+=l.count('W')+l.count('B')+l.count('G')
if c==m*n:
    print('#Black&White')
else:
    print('#Color')
