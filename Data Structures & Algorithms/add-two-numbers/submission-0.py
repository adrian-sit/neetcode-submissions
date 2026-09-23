# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        increment = False
        len1 = 0
        len2 = 0
        while curr1:
            curr1 = curr1.next
            len1 += 1
        while curr2:
            curr2 = curr2.next
            len2 += 1
        if len1 >= len2:
            curr1 = l1
            curr2 = l2
        else:
            curr1 = l2
            curr2 = l1

        while curr1:
            if increment:
                curr1.val += 1
                increment = False
            if curr2:
                curr1.val += curr2.val
                curr2 = curr2.next
            if curr1.val >= 10:
                increment = True
                curr1.val -= 10
            if not curr1.next and increment:
                new_node = ListNode(1)
                curr1.next = new_node
                break
            curr1 = curr1.next
            
        if len1 >= len2:
            return l1
        else:
            return l2



            

        