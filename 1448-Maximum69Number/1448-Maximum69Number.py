# Last updated: 8/5/2025, 2:54:14 PM
class Solution:
    def maximum69Number (self, num: int) -> int:
        max = num
        num_list = [int(d) for d in str(num)]
        if num < 9998:
            for ele in range(len(num_list)):
                if num_list[ele] == 6:
                    temp = num_list
                    temp[ele] = 9
                    temp = ''.join(str(x) for x in temp)
                    if max < int(temp):
                        num_list[ele] = 9
                        break
        return int(''.join(str(x) for x in num_list))