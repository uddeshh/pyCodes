n=int(input())
for i in range(n):
    word=input()
    if len(word)==2:
        print(word)
    else:
        wr_ls=[]
        mid=[]
        for j in word:
            wr_ls.append(j)
        for k in range(2,len(wr_ls)-1):
            if k%2!=0:
                mid.append(wr_ls[k])
        w=''.join(mid)
        print(word[:2]+w+wr_ls[len(wr_ls)-1])
