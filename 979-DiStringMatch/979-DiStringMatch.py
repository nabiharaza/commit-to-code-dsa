# Last updated: 8/5/2025, 2:56:17 PM
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        finalVal = []
        icount = 0
        dcount = len(S)
        for i in range(len(S)):
            if S[i] == 'I':
                finalVal.append(icount)
                icount += 1
            else:
                finalVal.append(dcount)
                dcount -= 1
        if dcount == icount:
            finalVal.append(dcount)
        return finalVal