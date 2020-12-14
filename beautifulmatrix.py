for i in range(5):
    line= list(map(int , input().split()))
    if 1 in line:
        k = line.index(1)
        j=i
steps = abs(k-2) + abs(j - 2)
print(steps)
