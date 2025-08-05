# Last updated: 8/5/2025, 2:55:55 PM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:    
        
        trusted = [0] * (n)
        trusted_by =  [0] * (n)
        
        for a,b in trust:
            trusted_by[a-1] +=1
            trusted[b-1]+=1
        
        for i in range(len(trusted)):
            if trusted[i] == n-1 and trusted_by[i] == 0:
                return i+1
        return -1
    