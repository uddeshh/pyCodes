import math
n= input()
sc = list(map(int,input().split()))
tot=[]
one=sc.count(1)
two=sc.count(2)
three=sc.count(3)
four=sc.count(4)
tot.append(four)
tot.append(three)
if three<=one:
    one=one-three
else:
    one=0

one=math.ceil(one/2)
o_t=math.ceil((two+one)/2)
tot.append(o_t)
print(sum(tot))
