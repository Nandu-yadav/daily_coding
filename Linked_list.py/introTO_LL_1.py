# No -> anywhere (that is only for diagrams). This is interview-ready code.

# 1. Node definition
class Node:
    def __init__(self, data):
        self.data = data      # stores value
        self.next = None      # reference to next node

# 2. Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

# 3. Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# 4. Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

# 5. Traverse / Print linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# 6. Delete a value
    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

# 7. Full working example
if __name__=="__main__":
    ll = LinkedList()

    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    ll.print_list()     # 5 10 20 30
    ll.delete(10)
    ll.print_list()     # 5 20 30
# Key interview clarifications (important)
# next is not built-in — you define it
# a.next = b is the actual link
# -> is only a diagram symbol, never Python code
# None marks the end of the list