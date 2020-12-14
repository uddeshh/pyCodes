n=int(input())
op=[]
for i in range(n):
    name = input()
    if name not in op:
        print('OK')
    else:
        print(name+str(op.count(name)))
    op.append(name)
#cant not be done
