p=input()
n=int(p,2)
m=int(input(),2)
r=str(bin(n^m))[2:]
l=len(p)
for i in range(l-len(r)):
    r='0'+r
print(r)
