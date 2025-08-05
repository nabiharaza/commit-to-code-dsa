# Last updated: 8/5/2025, 2:52:31 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        # current = head
        # st = []
        # maximumSum = 0

        # while current:
        #     st.append(current.val)
        #     current = current.next

        # current = head
        # size = len(st)
        # count = 1
        # maximumSum = 0
        # while count <= size/2:
        #     maximumSum = max(maximumSum, current.val + st.pop())
        #     current = current.next
        #     count = count + 1

        # return maximumSum

        # Get one pointer to the end of the linked list
        # right = head
        # pointers = []
        # count = 0
        # while right:
        #     count += 1
        #     pointers.append(right)
        #     right = right.next

        # # start calculating the sum of the twin nodes inward
        # left = 0
        # max_twin_sum = 0
        # while left > count:
        # # keep track of the max
        #     max_twin_sum = max(max_twin_sum, pointers[left].val + pointers[count].val)
        #     left += 1
        #     count -= 1

        # return max_twin_sum

        # T = O(N)
        # S = O(N)

        q = []
        right = head
        while right:
            q.append(right.val)
            right = right.next

        left = 0
        right = len(q)-1
        max_twin_sum = 0
        while left < right:
            max_twin_sum = max(max_twin_sum, q[left] + q[right])
            left += 1
            right -= 1
    
        return max_twin_sum

