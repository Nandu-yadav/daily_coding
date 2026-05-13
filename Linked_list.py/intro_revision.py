# ==========================================
# LINKED LIST USING OOP (Beginner Friendly)
# ==========================================


# ------------------------------------------
# 1. Create Node Class
# ------------------------------------------

class ListNode(object):

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next


# ------------------------------------------
# 2. Create Linked List
# ------------------------------------------

head = ListNode(10)

head.next = ListNode(20)

head.next.next = ListNode(30)

head.next.next.next = ListNode(40)


# Linked List Looks Like:
#
# 10 -> 20 -> 30 -> 40 -> None


# ------------------------------------------
# 3. Traverse / Print Linked List
# ------------------------------------------

print("Original Linked List:")

temp = head

while temp is not None:

    print(temp.val)

    temp = temp.next


# ------------------------------------------
# 4. Count Total Nodes
# ------------------------------------------

def countNodes(head):

    count = 0

    temp = head

    while temp is not None:

        count += 1

        temp = temp.next

    return count


print("\nTotal Nodes:", countNodes(head))


# ------------------------------------------
# 5. Search Element in Linked List
# ------------------------------------------

def search(head, target):

    temp = head

    while temp is not None:

        if temp.val == target:
            return True

        temp = temp.next

    return False


print("\nSearch 30:", search(head, 30))
print("Search 100:", search(head, 100))


# ------------------------------------------
# 6. Insert at Beginning
# ------------------------------------------

newNode = ListNode(5)

newNode.next = head

head = newNode


print("\nAfter Insert at Beginning:")

temp = head

while temp is not None:

    print(temp.val)

    temp = temp.next


# Linked List:
#
# 5 -> 10 -> 20 -> 30 -> 40


# ------------------------------------------
# 7. Insert at End
# ------------------------------------------

newNode = ListNode(50)

temp = head

while temp.next is not None:

    temp = temp.next

temp.next = newNode


print("\nAfter Insert at End:")

temp = head

while temp is not None:

    print(temp.val)

    temp = temp.next


# Linked List:
#
# 5 -> 10 -> 20 -> 30 -> 40 -> 50


# ------------------------------------------
# 8. Delete First Node
# ------------------------------------------

head = head.next


print("\nAfter Deleting First Node:")

temp = head

while temp is not None:

    print(temp.val)

    temp = temp.next


# Linked List:
#
# 10 -> 20 -> 30 -> 40 -> 50


# ------------------------------------------
# 9. Reverse Linked List
# ------------------------------------------

def reverseLinkedList(head):

    prev = None

    current = head

    while current is not None:

        nextNode = current.next

        current.next = prev

        prev = current

        current = nextNode

    return prev


head = reverseLinkedList(head)


print("\nAfter Reversing Linked List:")

temp = head

while temp is not None:

    print(temp.val)

    temp = temp.next


# Reversed:
#
# 50 -> 40 -> 30 -> 20 -> 10


# ------------------------------------------
# 10. Find Middle Node
# ------------------------------------------

def findMiddle(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

    return slow


middle = findMiddle(head)

print("\nMiddle Node:", middle.val)


# ------------------------------------------
# 11. Delete Last Node
# ------------------------------------------

temp = head

while temp.next.next is not None:

    temp = temp.next

temp.next = None


print("\nAfter Deleting Last Node:")

temp = head

while temp is not None:

    print(temp.val)

    temp = temp.next


# ------------------------------------------
# 12. Important Traversal Pattern
# ------------------------------------------

# temp = head
#
# while temp is not None:
#
#     # work on node
#
#     temp = temp.next


# ==========================================
# IMPORTANT CONCEPTS
# ==========================================

# self.val
# Stores data of node

# self.next
# Stores address/reference of next node

# head
# Starting node of linked list

# temp
# Used for traversal

# None
# End of linked list