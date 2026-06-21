# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        head = ListNode()
        res = head

        while curr1 and curr2:
            if curr1.val >= curr2.val:
                head.next = ListNode(curr2.val)
                head = head.next
                curr2 = curr2.next
            else:
                head.next = ListNode(curr1.val)
                head = head.next
                curr1 = curr1.next
            
        while curr1 or curr2:
            if curr1:
                head.next = ListNode(curr1.val)
                head = head.next
                curr1 = curr1.next
            if curr2:
                head.next = ListNode(curr2.val)
                head = head.next
                curr2 = curr2.next
        
        return res.next