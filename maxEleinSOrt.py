# t=int(input())
# for i in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
#     for i in range(n):
#         if l[i]<l[i-1] and l[i]>0:
#             print(l[i])
#             break
# a_angry,b_angry=input().split()
# if a_angry =='True':
#     if b_angry=='True':
#         print('True')
#     else:
#         print('False')
# else:
#     if b_angry=='False':
#         print('True')
#     else:
#         print('False')

#{
#Driver Code Starts
#Initial Template for Python 3



 # } Driver Code Ends

#User function Template for python3


# Function to print True and False for required input
def friends_in_trouble(a_angry, b_angry):
    ##Your code here
    if a_angry ==True:
        if b_angry==True:
            return 'True'
        else:
            return 'False'
    else:
        if b_angry==False:
            return 'True'
        else:
            return 'False'

#{
#Driver Code Starts.

# Driver code
def main():
    testcase = int(input())

    # loop for testcases
    while(testcase > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        if(string1 == 'True'):
            string1 = True
        else:
            string1 = False

        if(string2 == 'True'):
            string2 = True
        else:
            string2 = False

        print(friends_in_trouble(string1, string2))

        testcase -= 1

if __name__ == '__main__':
    main()
#} Driver Code Ends
