

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(7)
n2=Node(11)
n3=Node(3)
n4=Node(2)
n5=Node(9)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

def TraverseAndPrint(head):
    currentNode=head
    while currentNode:
        print(currentNode.data,end="->")
        currentNode =currentNode.next
    print("null")
    
TraverseAndPrint(n1)
#find the lowest Value in LL
def Lowest(head):
    minVal=head.data
    currNode=head.next
    while currNode:
        if currNode.data<minVal:
            minVal=currNode.data
        currNode=currNode.next
    return minVal
print(Lowest(n1))