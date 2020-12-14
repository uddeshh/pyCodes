def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
# def gcd(a,b):
#     if a==b:
#         return a
#     elif a==0 or b==0:
#         return a+b
#     elif a>b:
#         return gcd(a%b,b)
#     elif b>a:
#         return gcd(a,b%a)
a,b=map(int,input().split())
# # if a==b:
# #     x=fact(a)
# #     print(gcd(x,x))
# # else:
# #     x=fact(a)
# #     y=fact(b)
# #     print(gcd(x,y))
# a=int(input())
# print(fact(a))
x=fact(a) if a<b else fact(b)
print(x)
