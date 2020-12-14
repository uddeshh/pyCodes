n=input()
if int(n)>=0:
    print(n)
else:
    a=n[1:len(n)-1]
    b=n[1:len(n)-2]+n[len(n)-1:]
    ans=min(int(a),int(b))
    if ans==0:
        print(0)
    else:
        print(-1*ans)
