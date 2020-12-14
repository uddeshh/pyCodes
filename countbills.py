amount=input()
hun,tw,te,fv,on=0,0,0,0,0
he=len(amount)-2
hun=amount[:he]
if hun=='':
    hun=0
# print(hun)
rem=int(amount[he:])
tetw=int(rem/10)
if tetw%2==0:
    tw=int(tetw/2)
else:
    if tetw==1:
        te=1
    if tetw>2:
        tw=(tetw-1)/2
        te=1
# print(tw,te)
onfv=int(rem%10)
if (onfv)>=5:
    fv=1
    on=onfv-5
else:
    on=onfv%5
# print(fv,on)
print(int(hun)+int(tw)+int(te)+int(fv)+int(on))
