from typing import List, Set

# https://leetcode.com/problems/subsets/submissions/1609159580/
class Solution:
    def __init__(self):
        self.combinations: List[List] = list()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.combinations.append([])
        for i in range(0, len(nums)):
            for j in range(0, len(self.combinations)):
                n = list(self.combinations[j])
                n.append(nums[i])
                self.combinations.append(n)
        return self.combinations

def main():
    s = Solution()
    s.subsets([1, 2, 3])


if __name__ == "__main__":
    main()
