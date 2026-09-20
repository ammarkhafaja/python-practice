# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        res=ListNode()
        ress=ListNode()
        if list1 is None and list2 is None: return None
        elif list1 is None: return list2
        elif list2 is None: return list1
        if list1.val<list2.val:
            res=list1
            ress=list1
            list1=list1.next
        else:
            res=list2
            ress=list2
            list2=list2.next
        while list1 is not None or list2 is not None:
            if list1 is None:
                while list2 is not None:
                    res.next=list2
                    res=res.next
                    list2=list2.next
                return ress
            elif list2 is None:
                while list1 is not None:
                    res.next=list1
                    res=res.next
                    list1=list1.next
                return ress    
            if list1.val<list2.val:
                res.next=list1
                res=res.next
                list1=list1.next
            else:
                res.next=list2
                res=res.next
                list2=list2.next
        return ress
        

        