#DATA REPLACEMENT

class Solution:
    def removeNthFromEnd(self, head, n) :
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:           # deleting head
            return head.next

        while fast.next:       # IMPORTANT FIX
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
