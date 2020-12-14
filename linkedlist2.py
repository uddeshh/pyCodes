class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:

    def __init__(self):
        self.head=None

    def printit(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def insertit(self,data):
        newNode=Node(data)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode

    def findit(self,ele):
        current=self.head
        c=0
        while current:
            if current.data==ele:
                print(c)
            c+=1
            current=current.next

    def dontinsert(self,ele):
        temp=self.head
        if temp is not None:
            if temp.data==ele:
                self.head=temp.next
                temp=None
                return
        while temp is not None:
            if temp.data==ele:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None

    def searchit(self,ele):
        current=self.head
        while current:
            if current.data==ele:
                print('YES')
            current=current.next
        else:
            print('No')

l=list(map(int,input().split()))
ele=int(input())
ll=Linkedlist()
for i in l:
    ll.insertit(i)
ll.dontinsert(ele)
# ll.printit()
