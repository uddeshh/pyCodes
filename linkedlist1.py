class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printit(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def insertit(self,data):
        newNode=node(data)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
l=list(map(int,input().split()))
ll=linkedlist()
for i in l:
    ll.insertit(i)
ll.printit()












# if __name__=='__main__':
#     llist=linkedlist()
#     llist.head=node(1)
#     second=node(2)
#     third=node(3)
#     fourth=node(4)
#     llist.head.next=second;
#     second.next=third;
#     third.next=fourth;
#     llist.printit()

# l=list(map(int,input().split()))
# llist=linkedlist()
# for i in range(l):











#
# A simple Python program for traversal of a linked list
#
# # Node class
# class Node:
#
# 	# Function to initialise the node object
# 	def __init__(self, data):
# 		self.data = data # Assign data
# 		self.next = None # Initialize next as null
#
#
# # Linked List class contains a Node object
# class LinkedList:
#
# 	# Function to initialize head
# 	def __init__(self):
# 		self.head = None
#
# 	# This function prints contents of linked list
# 	# starting from head
# 	def printList(self):
# 		temp = self.head
# 		while (temp):
# 			print (temp.data)
# 			temp = temp.next
#
#
# # Code execution starts here
# if __name__=='__main__':
#
# 	# Start with the empty list
# 	llist = LinkedList()
#
# 	llist.head = Node(1)
# 	second = Node(2)
# 	third = Node(3)
#
# 	llist.head.next = second; # Link first node with second
# 	second.next = third; # Link second node with the third node
#
# 	llist.printList()
