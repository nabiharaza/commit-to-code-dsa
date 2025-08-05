# Last updated: 8/5/2025, 2:52:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head.next is None:
        #     return None

        # slow = head
        # fast = head.next.next

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # slow.next = slow.next.next
        # return head

        if not head:
            return None
        
        if not head.next:
            return None

        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        
        mid_node = floor(size/2)

        cur = head
        size = 0
        while size != mid_node:
            size += 1
            prev = cur
            cur = cur.next

        prev.next = cur.next

        return head