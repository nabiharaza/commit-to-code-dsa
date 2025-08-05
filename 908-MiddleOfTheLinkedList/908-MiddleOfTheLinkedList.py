# Last updated: 8/5/2025, 2:56:37 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leftPtr = rightPtr = head
        while rightPtr and rightPtr.next:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next.next
        return leftPtr