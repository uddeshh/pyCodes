word = input()
l=[]
for i in word:
    l.append(i)
letter=ord(l[0])
if 122>=letter>=97:
    new_value = letter-32
    l[0]=chr(new_value)
final = ''.join(l)
print(final)

# for i in word:
#     letter = ord(i)
#     if 122>letter>97:
#         new_value = letter-32
#         i=chr(new_value)
#         break
# print(word)
