# Last updated: 8/5/2025, 2:56:19 PM
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = dict()
        isFound = False
        itr = N
        while itr > 0:
            if not isFound:
                state_key = tuple(cells)
                if state_key in seen:
                    itr %= seen[state_key] - itr
                    isFound = True
                else:
                    seen[state_key] = itr
            if itr > 0:
                cells = self.updateCells(cells)
                itr -= 1    
        return cells
    
    def updateCells(self, cells):
        ret = []
        ret.append(0)
        for ele in range(1, len(cells) - 1):
            ret.append(int(cells[ele - 1] == cells[ele + 1]))
        ret.append(0)
        return ret