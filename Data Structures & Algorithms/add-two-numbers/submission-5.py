# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        carryover = 0

        result_head = ListNode()
        traversal_new_head = result_head
        while h1 is not None or h2 is not None or carryover != 0:

            val1 = 0
            if h1:
                val1 = h1.val
            
            val2 = 0
            if h2:
                val2 = h2.val
            
            sum = val1 + val2 + carryover

            if sum >= 10:
                carryover = sum // 10
                sum = sum % 10
            else:
                carryover = 0
            traversal_new_head.next = ListNode(sum)
            traversal_new_head = traversal_new_head.next
            
            if h1:
                h1 = h1.next
            
            if h2:
                h2 = h2.next
        
        return result_head.next
            



            
            