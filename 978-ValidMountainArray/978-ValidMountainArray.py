# Last updated: 8/5/2025, 2:56:20 PM
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:                              
        if len(arr) < 3:
            return False
        l_a = True
        r_a = True
        l_p = 0
        r_p =len(arr) - 1
        while l_a or r_a :
            
            if arr[l_p] >= arr[l_p + 1] :
                l_a = False
            if arr[r_p] >= arr[r_p - 1]:
                r_a = False
            if l_a:
                l_p +=1
            if r_a:
                r_p -=1
            if l_p == r_p:
                break

        return l_p == r_p and l_p != 0 and r_p != len(arr) - 1  
 
    
    
#     EDGE CASES SHOULD BE ABOUT DEALING WITH DIFFERENT SITUATIONS OR DIFFERENT COMBINATIONS OF SITUATIONS
#     WHEN THINKING OF DONT TRY TO REPEAT THE SAME CASE 
    
    
#     = [3,5,6]
#            ^   
#            ^
        
#     = [1,2,3,4,5]
    
#     = []
    