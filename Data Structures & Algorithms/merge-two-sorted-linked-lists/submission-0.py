# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        new = ListNode()
        res = new
        while curr1 and curr2:
            val1 = curr1.val
            val2 = curr2.val
            print(new.val)
            if val1 <= val2:
                new.next = ListNode(val1)
                new = new.next
                curr1 = curr1.next
            else:
                new.next = ListNode(val2)
                new = new.next
                curr2 = curr2.next
            print(new.val)
    
        while curr1 or curr2:
            if curr1:
                new.next = ListNode(curr1.val)
                curr1 = curr1.next
                new = new.next
            if curr2:
                new.next = ListNode(curr2.val)
                curr2 = curr2.next
                new = new.next
        return res.next
