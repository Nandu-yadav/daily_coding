class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        cnt=0
        while temp!=None:
            cnt+=1
            temp=temp.next
        
        midNode=cnt//2
        temp=head
        while(temp!=None):
            if midNode==0:
                break
            temp=temp.next
            midNode-=1
        return temp
    
#OPTIMAL

class Solution:
    def middleNode(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

