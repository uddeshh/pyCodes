n = int(input())
add=[]
for i in range(n):
    s = input()
    if '+' in s:
        add.append(1)
    elif '-' in s:
        add.append(-1)
    else:
        continue
print(sum(add))
