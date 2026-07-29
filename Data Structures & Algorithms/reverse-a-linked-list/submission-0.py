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
        prev = None
        if curr2 is None:
            return curr1

        while True:
            curr3 = curr2.next
            curr2.next = curr1
            curr1.next = prev
            if curr3 is None:
                return curr2
            prev = curr2
            curr1 = curr3
            curr2 = curr1.next
            if curr2 is None:
                curr1.next = prev
                return curr1

            

    