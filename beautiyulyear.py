n = input()
p=int(n)+1
while True:
    if len(str(p))==len(set(str(p))):
        print(p)
        break
    else:
        p=p+1
