# a,b=map(int,input().split())
# c=0
# if min(a,b)==1:
#     print(1)
# else:
#     for i in range(1,int(min(a,b)/2)+1):
#         if a%i==0 and b%i==0:
#             c+=1
#     print(c,i)
# n=int(input())
# l=list(map(int,input().split()))
# l.sort()
# tot=int(sum(l)/n)
# for i in l:
#     if i-tot>0:
#         print(i)
#         break
# def gcd(a,b):
#     if a==0 or b==0:
#         return b+a
#     elif a>b:
#         return gcd(a%b,b)
#     else:
#         return gcd(a,b%a)
# a,b=map(int,input().split())
# n=gcd(a,b)
# # print(n)
# c=0
# for i in range(1,n+1):
#     if a%i==0 and b%i==0:
#         c+=1
#         print(i)
def gcd(a,b):
    if a==0:
        return b
    return (b%a,a)
a,b=map(int,input().split())
print(gcd(a,b))
