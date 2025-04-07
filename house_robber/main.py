from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        l1, l2 = 0, 0
        for i in nums:
            tmp = max(l1+i, l2)
            l1 = l2
            l2 = tmp
        return max(l1, l2)


def main():
    s = Solution()
    print(s.rob([2, 3, 2]))


if __name__ == "__main__":
    main()
