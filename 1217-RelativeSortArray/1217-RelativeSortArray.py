# Last updated: 8/5/2025, 2:54:57 PM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = dict()
        itr = 0
        temp = []
        for ele in range(len(arr2)):
            indices = [i for i, x in enumerate(arr1) if x == arr2[ele]]
            for indx in range(len(indices)):
                res[itr] = arr1[indices[indx]]
                itr += 1
        for ele in range(len(arr1)):
            if arr1[ele] not in res.values():
                temp.append(arr1[ele])
        temp.sort()
        for ele in range(len(temp)):
            res[itr] = temp[ele]
            itr += 1
        return list(res.values())