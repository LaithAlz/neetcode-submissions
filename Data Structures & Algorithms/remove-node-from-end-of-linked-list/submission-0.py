# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        length = 0
        while curr:
            curr = curr.next
            length += 1
        print(length)

        counter = length - n
        dummy = ListNode(0, head)
        curr = dummy

        while counter != 0:
            curr = curr.next
            counter -= 1
        
        to_delete = curr.next
        curr.next = to_delete.next


        return dummy.next
