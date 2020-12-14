name= input()
arr=[i for i in name]
unique_list=[]
for i in arr:
    if i not in unique_list:
        unique_list.append(i)
l = len(unique_list)
if l%2!=0:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')
