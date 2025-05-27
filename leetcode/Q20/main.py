from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, curset = [], []
        self.buildSubsets(0, nums, subset, curset)
        return subset

    def buildSubsets(self, i: int, nums: List[int], subset: List[List[int]], curset: List[List[int]]):
        if i >= len(nums):
            subset.append(curset.copy())
            return

        curset.append(nums[i])
        self.buildSubsets(i+1, nums, subset, curset)
        curset.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        self.buildSubsets(i+1, nums, subset, curset)


def main():
    s = Solution()

    print(s.subsetsWithDup([1, 2, 3, 3, 2, 2, 2, 4]))


if __name__ == "__main__":
    main()
