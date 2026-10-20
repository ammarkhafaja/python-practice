# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode | None):
    if head==None:return head
    list=[]
    list.append(head.val)
    prev=head
    curr=head.next
    while curr != None:
        if not curr.val in list:
            list.append(curr.val)
            prev=curr
            curr=curr.next
        else:
            if curr.next==None:
                prev.next=None
                curr=curr.next
                
            else:
                prev.next=curr.next
                curr=curr.next
    return head

        
            

