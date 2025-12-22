class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Reverse a linked list (recursive)
def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_linked_list(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head


# Check if linked list is palindrome
def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find middle using slow & fast pointers
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second_half_head = reverse_linked_list(slow.next)

    # Compare both halves
    first = head
    second = second_half_head
    is_pal = True

    while second:
        if first.data != second.data:
            is_pal = False
            break
        first = first.next
        second = second.next

    # Restore original list
    slow.next = reverse_linked_list(second_half_head)

    return is_pal


# Print linked list
def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Driver code
if __name__ == "__main__":
    # Create linked list: 1 -> 5 -> 2 -> 5 -> 1
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    print("Original Linked List:", end=" ")
    print_linked_list(head)

    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")
