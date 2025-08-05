# Last updated: 8/5/2025, 2:55:04 PM
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        for ele in range(1, len(arr) - 1):
            temp_arr = []
            temp_arr.extend(arr)
            for item in range(1, len(arr) - 1):
                if arr[item] < arr[item - 1] and arr[item] < arr[item + 1]:
                    temp_arr[item] += 1
                elif arr[item] > arr[item - 1] and arr[item] > arr[item + 1]:
                    temp_arr[item] -= 1
            arr.clear()
            arr.extend(temp_arr)
        return arr