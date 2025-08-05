# Last updated: 8/5/2025, 2:56:27 PM
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge(L,R,nums):   # Function  to merge sorted arrays
            i = 0
            j = 0
            k = 0
            while i<len(L) and j<len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i+=1
                    k+=1
                else :
                    nums[k] = R[j]
                    j+=1
                    k+=1
            while i<len(L):
                nums[k] = L[i]
                i+=1
                k+=1
            while j<len(R):
                nums[k] = R[j]
                j+=1
                k+=1
            # Merging done
            return nums

        def mergeSort(nums):   

            l = len(nums)
            if l == 1:
                return nums
            if l%2 == 0:
                mid_index = l/2 - 1 
            else :
                mid_index = (l-1)/2
            
            # Get the left and right arrays
            L = nums[0:mid_index +1]
            R = nums[mid_index+1:l]

            # Sort them recursively
            L = mergeSort(L)
            R = mergeSort(R)

            # Merge sorted L and R
            nums_sorted = merge(L,R,nums)
            return nums_sorted
            
        nums = mergeSort(nums)
        return nums

