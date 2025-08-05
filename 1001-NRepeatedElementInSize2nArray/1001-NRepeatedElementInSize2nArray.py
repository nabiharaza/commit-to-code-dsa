# Last updated: 8/5/2025, 2:56:11 PM
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A_dict = dict()
        for ele in range(len(A)):
            if A[ele] not in A_dict:
                A_dict[A[ele]] = 1
            else:
                return A[ele]