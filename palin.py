# t=int(input())
# for k in range(t):
#     s=input()
#     n=len(s)
#     tot=[]
#     for i in range(n):
#         for j in range(i,n):
#             X=s[i:j+1]
#             if X==X[::-1] and X not in tot:
#                 tot.append(X)
#     print(tot)
# s=input()
# n=len(s)
# for i in range(n):
#     for j in range(i,n):
#         print(s[i:j+1])

# t=int(input())
# for i in range(t):
#     N=int(input())
#     M=list(map(int,input().split()))
#     mat=[]
#     k=0
#     while k<N+1:
#         mat.append(M[k*N:k*N+N])
#         k+=1
#     print(mat)
#     res=[]
#     for i in range(N):
#         for j in range(N):
#             res.append(mat[j][i])
#     print(res)

# t=int(input())
# for i in range(t):
#     S=input()
#     s=list(input())
# print(2**32)
def gcd(A, B):
    if A>B:
        return gcd(A-B,B)
    elif B>A:
        return gcd(A,B-A)
    elif A==B:
        return A
print(gcd(3,1))
