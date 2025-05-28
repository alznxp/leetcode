# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, sum, prev = head.next, 0, head

        while curr:
            sum += curr.val
            if curr.val == 0:
                curr.val, sum = sum, 0
                prev.next = prev = curr
            curr = curr.next
        
        return head.next