n = input()
s = input()
a = [i for i in s if i=="A"]
b = [i for i in s if i=="D"]
if len(a)>len(b):
    print('Anton')
elif len(a)<len(b):
    print('Danik')
else:
    print('Friendship')
