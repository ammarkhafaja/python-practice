# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        first=True
        if head is None:
            return None
        else:
            res=ListNode()
            while head != None:
                if first:
                    res.val=head.val
                    head=head.next
                    first=False
                    continue
                cur=ListNode(val=head.val)
                cur.next=res
                res=cur
                head=head.next
            return res



