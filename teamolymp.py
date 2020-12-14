n= int(input())
sp=list(map(int,input().split()))

one=sp.count(1)
two=sp.count(2)
three=sp.count(3)
team=min(one,two,three)
if one!=0 or two!=0 or three!=0:
    print(team)
    for i in range(team):
        # print(sp)
        print(sp.index(1)+1,sp.index(2)+1,sp.index(3)+1)
        sp.insert(sp.index(1),0)
        sp.remove(1)
        sp.insert(sp.index(2),0)
        sp.remove(2)
        sp.insert(sp.index(3),0)
        sp.remove(3)
        # print(sp)
else:
    print(0)
