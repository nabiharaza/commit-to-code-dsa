# Last updated: 8/5/2025, 2:54:25 PM
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums_dict = OrderedDict()
        for i in range(len(nums)):
            self.add(nums[i])

    def showFirstUnique(self) -> int:
        for k, v in self.nums_dict.items():
            if v == True:
                return k
        return -1

    def add(self, value: int) -> None:
        if value not in self.nums_dict:
            self.nums_dict[value] = True
        else:
            self.nums_dict[value] = False

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)