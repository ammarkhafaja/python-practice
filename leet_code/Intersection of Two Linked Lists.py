
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:

# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if headA is None or headB is None:
        return None
    pa, pb = headA, headB
    while pa is not pb:
        pa=pa.next if pa else headB
        pb=pb.next if pb else headA
    return pa