# Last updated: 8/5/2025, 2:54:37 PM
#hashmap /set

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = {}
        for a in arr:
            arr_dict[a] = arr_dict.get(a, 0) + 1
            # print(arr_dict)
        return len(arr_dict) == len(set(arr_dict.values()))

# tc - o(n)
# sc - o(n)