#make up a stack and store all the elements and check from first to last of LL to stack elements(last in first out)
#optimal
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def reverseList(self, head):
        #using Recursion
        if head==None or head.next==None:
            return head
        newHead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newHead
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


