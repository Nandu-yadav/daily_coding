'''
If you want to delete a node in a linked list, it is important to connect the nodes on each side of the node before deleting it, so that the linked list is not broken.

So before deleting the node, we need to get the next pointer from the previous node, and connect the previous node to the new next node before deleting the node in between.

Also, it is a good idea to first connect next pointer to the node after the node we want to delete, before we delete it. This is to avoid a 'dangling' pointer, a pointer that points to nothing, even if it is just for a brief moment.

The simulation below shows the node we want to delete, and how the list must be traversed first to connect the list properly before deleting the node without breaking the linked list.
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverseAndPrint(head):
    currentNode=head
    while currentNode:
        print(currentNode.data,end="->")
        currentNode=currentNode.Next
    print("null")
def deleteNode(head,nodeToDelete):
    if head==nodeToDelete:
        return head.next
    currentNode=head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode=currentNode.next
    if currentNode.next is None:
        return head
    currentNode.next=currentNode.next.next
    return head
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)