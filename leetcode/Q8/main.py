from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        # nums.reverse()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res

    def getNextStart(self, nums: List[int], remainder: int) -> int:
        for idx, item in enumerate(nums):
            if item <= remainder:
                return idx


def main():
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))


if __name__ == "__main__":
    main()
