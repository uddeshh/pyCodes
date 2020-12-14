def longword():
    n = int(input())
    lst=[]
    for i in range(n):
        w = input()
        sw=[]
        for j in w:
            sw.append(j)
        l=len(sw)
        f=sw[0]
        e=sw.pop()
        if l<=10:
            lst.append(w)
        else:
            lw = [f,str(l-2),e]
            new = ''.join(lw)
            lst.append(new)
    for i in lst:
        print(i)

longword()
