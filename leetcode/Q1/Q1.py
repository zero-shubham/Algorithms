# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def removeDuplicates(self) -> int:
        nums = self.nums
        i = 0
        j = i+1

        curr_count = 1

        while j < len(nums):
            if nums[j] == nums[i]:
                curr_count += 1

                if curr_count <= 2:
                    i += 1
                    if nums[i] != nums[i-1]:
                        nums[i] = nums[i-1]
            else:
                i += 1

                nums[i] = nums[j]
                curr_count = 1

            j += 1

        print(nums)
        nums[i] = nums[j-1]
        self.nums = nums[:i+1]

        return i+1


s = Solution([1, 1, 1, 1, 2, 2, 3])
print(s.removeDuplicates())
print("nums = ", s.nums)

s = Solution([0, 0, 1, 1, 1, 1, 2, 3, 3])
print(s.removeDuplicates())
print("nums = ", s.nums)
