# Last updated: 8/5/2025, 2:56:31 PM
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        I=D=1
        for i in range(len(nums)-1):
            if nums[i+1]>=nums[i]:
                I=I*1
            else:
                I=I*0
            
            if nums[i+1]<=nums[i]:
                D=D*1
            else:
                D=D*0
        
        return I+D
            
                