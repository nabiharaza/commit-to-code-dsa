# Last updated: 8/5/2025, 2:54:23 PM
#hash set

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))

        # answer = []
        # answer.append(list(set(nums1) - set(nums2)))
        # answer.append(list(set(nums2) - set(nums1)))
        # return answer

        # answer = [[],[]]
        # set1 = set(nums1)
        # set2 = set(nums2)

        # for num in set1:
        #     if num not in set2:
        #         answer[0].append(num)

        # for num in set2:
        #     if num not in set1:
        #         answer[1].append(num)

        # return answer

# applies to all above soln's:
# tc / sc - o(n + m)