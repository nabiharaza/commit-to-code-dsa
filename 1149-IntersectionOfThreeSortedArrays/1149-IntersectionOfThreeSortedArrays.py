# Last updated: 8/5/2025, 2:55:38 PM
def binary_search(arr,target):
    l , r = 0 , len(arr) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid
        else:
            r = mid
    if arr[l] == target: return True
    if arr[r] == target: return True
    return False

class Solution:
    # def binary_search(arr,target):
    #     l , r = 0 , len(arr) - 1
    #     while l + 1 < r:
    #         mid = (l + r) // 2
    #         if arr[mid] == target:
    #             return mid
    #         if arr[mid] < target:
    #             l = mid
    #         else:
    #             r = mid
    #     if arr[l] == target: return True
    #     if arr[r] == target: return True
    #     return False

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        output = [] 
        for i in arr1:
            if binary_search(arr2, i) and binary_search(arr3, i):
                output.append(i)
        return output        