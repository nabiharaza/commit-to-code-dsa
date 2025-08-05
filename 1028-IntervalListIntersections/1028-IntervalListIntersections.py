# Last updated: 8/5/2025, 2:56:00 PM
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i,j = 0,0

        while i < len(firstList) and j < len(secondList):
            start_a = firstList[i][0]
            end_a = firstList[i][1]

            start_b = secondList[j][0]
            end_b = secondList[j][1]

            start = max(start_a,start_b)
            end = min(end_a,end_b)

            if start <= end:
                res.append([start, end])
            
            if end_a <= end_b:
                i += 1
            else:
                j += 1
        
        return res