# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None

        curr1 = head
        curr2 = head.next
        if curr2 is None:
            return curr1
        curr1.next = None

        while True:
            curr3 = curr2.next
            curr2.next = curr1
            if curr3 is None:
                return curr2
            curr1 = curr2
            curr2 = curr3

            

    