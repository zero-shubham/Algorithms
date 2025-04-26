from typing import List


class Solution:
     def canJump(self, nums: List[int]) -> bool:
        prev = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            j = nums[i]

            if i+j >= prev:
                prev = i

        return prev==0


def main():
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))


if __name__ == "__main__":
    main()
