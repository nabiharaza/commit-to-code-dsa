# Last updated: 8/5/2025, 2:54:18 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_nums = 0
        for i in nums:
            s = len(str(i))
            if s%2 == 0 :
                even_digit_nums +=1
            else:
                pass
            
            
    
        return even_digit_nums
            