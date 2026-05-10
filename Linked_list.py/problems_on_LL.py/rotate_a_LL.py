
def findNthNode(temp,k):
    cnt=1
    while(temp != None):
        if cnt==k:
            return temp
        cnt+=1
        temp =temp.next
    return temp


def RotateLLbyK(head, k):
    if (head=None or k==0):
        return head
    length=1
    tail=head
    while(tail.next!=None):
        tail=tail.next
        length+=1

    if k%length==0:
        return head
    k=k%length
    tail.next=head
    newLastNode = findNthNode(head,length-k)
    head=newLastNode.next
    newLastNode.next=None
