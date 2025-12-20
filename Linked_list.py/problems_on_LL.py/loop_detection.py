class Solution:
    def hasCycle(self, head):
        visited = set()
        temp = head

        while temp is not None:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next

        return False

#OPTIMAL
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next: #TAKE fast.next not something else like "slow", beacuse:if fast.next is none it will raise an error
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
    
