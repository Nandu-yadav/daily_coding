
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.back=None

# def countElements(self,head):
#     if head==None:
#         return 0
#     elif head.next==None:
#         return 1
#     cnt=1
#     temp=head
#     while temp:
#         temp=temp.next
#         cnt+=1
#     return cnt

# #delete Last elemnt

# def DeleteLast(head):
#     if head==None or head.next==None:
#         return None
#     temp=head
#     while temp.next.next:
#         temp=temp.next
#     temp.next=None
#     return head

# def DeleteKposition(head,k):
#     if head ==None:
#         return None
#     if head.data==k:
#         return None
#     temp=head
#     while temp :
#         temp=temp.next
#         if temp.data==k:
#             prev=temp
#             temp=temp.next
#             prev.next=prev.next.next
#             temp.next=None
#     return head

# #INsert at a position

# def InsertatKposition(head,k):
#     newHead=Node(k)
#     if head ==None:
#         return None
#     if head.data==k:
#         return None
#     temp=head
#     cnt=0
#     while temp :
#         cnt+=1
#         temp=temp.next
        
#         if cnt==k-1:
#             n=newHead(k)
#             n.next=temp.next
#             temp.next=n
#         temp=temp.next
#     return head


# #------------------------------------------------------------------------------------
# #DOubly LInked LIst
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.back=None
# def Node(data1,next1,back1):
#     data=data1
#     next=next1
#     back=back1


# def convertArrDDL(arr):
#     head=Node(arr[0])
#     prev=head
#     for x in arr:
#         temp= Node(x,None,prev)
#         prev.next=temp
#         prev=temp
#     return head
# def print1(head):
#     while head:
#         print(head.data,end=" ")
#         head=head.next

# arr=[12,5,4,3,2]

# head=convertArrDDL(arr)
# print(head)



# #Delete head
# def delete(prev):
#     prev.back=None
#     prev.next=None

# def deleteHead(head):
#     if head==None or head.next==None:
#         return None
#     prev =head
#     head=head.next

#     head.back=None
#     prev.next=None

#     delete(prev)
#     return head

# def removeKthElement(head,k):
#     if head==None:
#         return None
#     cnt=0
#     kNode=head
#     while(kNode != None):
#         cnt+=1
#         if cnt==k:
#             break
#         kNode=kNode.next
#     prev=kNode.back
#     front=kNode.next

#     if prev==None and front==None:
#         return None
#     delete(kNode)
#     return head

# print(removeKthElement(head,k))




def AddnumbersInLL(head1,head2):
    t1=head1
    t2=head2
    dummy=Node(-1)
    curr=dummy
    carry=0
    while t1 or t2:
        sum=carry
        if t1:
            sum=sum+t1.data
        if t2:
            sum=sum+t2.data
        newNode=Node(sum%10)
        curr.next=newNode
        curr=curr.next
    if t1:
        sum=sum+t1.data

#-----------------------------------------------------------------------------------
def sort012(head):
    if head==None or head.next==None:
        return head
    cnt0=0
    cnt1=0
    cnt2=0
    temp=head
    while temp:
        if temp.data==0:
            cnt0 += 1
        if temp.data==1:
            cnt1 += 1
        if temp.data==2:
            cnt2 += 1
        temp=temp.next
    temp=head
    while temp:
        if cnt0>0:
            temp.data=0
            cnt0 -= 1
            temp=temp.next
        elif cnt1>0:
            temp.data=1
            cnt1-=1
            temp=temp.next
        elif cnt2>0:
            temp.data=2
            cnt2-=1
            temp=temp.next
    return head

def sort012Optimal(head):
    if head==None or head.next==None:
        return head
    #change the link
    temp=head
    zeroHead=Node(-1)
    zero=zeroHead
    oneHead=Node(-1)
    one=oneHead
    twoHead=Node(-1)
    two=twoHead

    while temp:
        if temp.data==0:
            zero.next=temp
            zero=zero.next
        elif temp.data==1:
            one.next=temp
            one=one.next
        elif temp.data==2:
            two.next=temp
            two=two.next
        temp=temp.next
    

    if oneHead!=None:
        zero.next=oneHead
    elif twoHead !=None:
        zero.next=twoHead
    if twoHead !=None or one != None:
        one.next=twoHead
    return head

#---------------------------------------------------------------------------------------------------
def intersectionOfYLink(head1,head2):
    if head1==None or  head2==None:
        return head1
    t1=head1
    t2=head2
    while t1 != t2:   #important
        t1=t1.next
        t2=t2.next
        if t1==t2:
            return t1
        
        if t1==None:
            t1=head2
        if t2==None:
            t2=head1
    return t1
        
#------------------------------------------------------------------------------
def DetectStarting(head):
    if head==None or head.next==None:
        return head
    fast=head
    slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.nextnext
        if fast==slow:
            slow=head
            while slow !=fast:
                slow=slow.next
                fast=fast.next        
            return slow
    return None
#----------------------------------------------------------------------------------
def LeangthOfLoop(head):
    if head==None or head.next==None:
        return head
    fast=head
    slow=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.nextnext
        if fast==slow:
            break
    cnt=1
    slow=slow.next
    while(fast!=slow):
        slow=slow.next
        cnt+=1
    return cnt

#=----------------------------------------------------------------------------------------
#REVERSE NODES IN K GROUPS
def ReverseNodesInKgroup(head,k):
    if head==None or head.next==None:
        return head
    temp=head
    cnt=0
    while temp:
        