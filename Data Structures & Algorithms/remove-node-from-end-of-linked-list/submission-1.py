# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length == n:
            return head.next

        remove = length - n
        curr = head
        while remove > 1:
            curr = curr.next
            remove -= 1

        if n == 1:
            curr.next = None
        else:
            curr.next = curr.next.next

        return head
