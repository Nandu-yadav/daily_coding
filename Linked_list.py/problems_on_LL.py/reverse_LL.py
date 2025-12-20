
#one brute way is to use STACKS and (last in first out)
class Solution:
    def reverseList(self, head):
        if not head:
            return head   
        stack = []
        temp = head
        # Push nodes onto stack
        while temp:
            stack.append(temp)
            temp = temp.next
        # New head is last node
        head = stack.pop()
        temp = head    
        # Rebuild links
        while stack:
            node = stack.pop()
            temp.next = node
            temp = node
        temp.next = None
        return head


#ITERATIVE WAY
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=None         #declaring the previous which is Nonea at first
        temp=head          # starting both temp and front from first
        front=head
        
        while temp:
            front=temp.next   # moving the front to next,   so now front has the next element
            temp.next=prev    # now moving link from front to previous (None) 
            prev=temp         #moving previous to temp position,
            temp=front         # temp to frot and now both temp and front same elment(next elemnt now) 
        return prev
#optimal
class Solution:
    def reverseList(self, head):
        #using Recursion
        if head==None or head.next==None:
            return head
        newHead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newHead