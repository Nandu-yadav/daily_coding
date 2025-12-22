# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#BETTER
class Solution:
    def findLength(self,head):
        if head==None :
            return 0
        temp=head
        cnt=0
        while temp:
            temp=temp.next
            cnt+=1
        return cnt
    def collision(self,head1,head2,N):
        temp1=head1
        temp2=head2
        while N>0:
            temp1=temp1.next
            N-=1
        while temp1 and temp2:
            if temp1==temp2:
                return temp1

            temp1=temp1.next
            temp2=temp2.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1=self.findLength(headA)
        n2=self.findLength(headB)
        if n1>=n2:
            return self.collision(headA,headB,n1-n2)
        else:
            return self.collision(headB,headA,n2-n1)
        
