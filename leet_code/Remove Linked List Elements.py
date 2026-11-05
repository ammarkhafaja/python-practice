class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
    cur=ListNode(0,head)
    head=cur
    while cur.next:
        if cur.next.val==val:
            cur.next=cur.next.next
        else:cur=cur.next
    return head.next