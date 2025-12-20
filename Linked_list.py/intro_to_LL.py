'''
Mapping (C++ → Python)
class Node → Python class
Node* next → self.next (reference, no pointers needed)
Constructors → __init__
vector<int> → Python list
cout << y->data → print(y.data)
This is idiomatic Python and functionally identical.
''' '''
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

if __name__ == "__main__":
    arr = [2, 5, 8, 7]
    y = Node(arr[0], None)
    print(y.data)
'''

# Simple Linked List Implementation in Python
class Node:
    def __init__(self, x):
        self.data = x      # store value
        self.next = None   # pointer to next node
class Test:
    def main():
        # create nodes like:new Node(10),new Node(20),new Node(30)
        head = Node(10)
        temp1 = Node(20)
        temp2 = Node(30)
        # link them: head -> temp1 -> temp2
        head.next = temp1
        temp1.next = temp2
        # traverse and print the list
        current = head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    Test.main()
