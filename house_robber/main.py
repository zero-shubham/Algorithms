from typing import List


class Solution:
    def get_largest_index(self, arr: List[int]) -> int:
        largest = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[largest]:
                largest = i

        return largest

    def rob(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        largest_idx = self.get_largest_index(nums)
        first_half = []
        if largest_idx-1 > 0:
            first_half = nums[:largest_idx-1]

        second_half = []
        if largest_idx+1 < len(nums):
            second_half = nums[largest_idx+2:]
        print("largest idx: ", largest_idx)
        print("first half: ", first_half)
        print("second half: ", second_half)
        largest_num = self.rob(
            first_half) + nums[largest_idx] + self.rob(
            second_half)
        return largest_num


def main():
    s = Solution()
    print(s.rob([2, 3, 2]))


if __name__ == "__main__":
    main()
