# def max_prof(arr):
#     n=len(arr)
#     profit=[0]*n
#     print(profit)
#     max_price=arr[n-1]
#     for i in range(n-2,0,-1):
#         if arr[i]>max_price:
#             max_price=arr[i]
#
#         profit[i]=max(arr[i+1],max_price-arr[i])
#     print(profit)
#     min_price=arr[1]
#     for i in range(1,n-1):
#         if arr[i]<min_price:
#             min_price=arr[i]
#
#         profit[i]=max(profit[i-1], profit[i]+(arr[i]-min_price))
#     print(profit)
#     return profit[n-1]

# ==================================================================================================================
# ============================================================================================================
# def maxProfit(price,n):
#     profit = [0]*n
#     max_price=price[n-1]
#     for i in range( n-2, 0 ,-1):
#         if price[i]> max_price:
#             max_price = price[i]
#         profit[i] = max(profit[i+1], max_price - price[i])
#     print(profit)
#     min_price=price[0]
#     for i in range(1,n):
#         if price[i] < min_price:
#             min_price = price[i]
#         profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
#     print(profit)
#     result = profit[n-1]
#     return result
# price=list(map(int,input().split()))
# n=len(price)
# print(maxProfit(price,n))
