class Node:

    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

    def printit(self):
        if self.left:
            self.left.printit()
        print(self.data)
        if self.right:
            self.right.printit()

    def insertit(self,data):
        # self.data=data
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insertit(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insertit(data)
        else:
            self.data=data

Root=Node(15)
Root.insertit(11)
Root.insertit(3)
Root.insertit(51)
Root.insertit(9)
Root.printit()
