from typing import List

# https://leetcode.com/problems/product-of-array-except-self/submissions/1624209012/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []

        for idx, n in enumerate(nums):
            prefix_prod.append(n * prefix_prod[idx-1] if idx > 0 else n)

        prev_prod = 1
        for idx, n in enumerate(reversed(nums)):
            curr_idx = (len(nums)-1)-idx
            # print(curr_idx,  prefix_prod, n, prev_prod)
            if curr_idx > 0:
                prefix_prod[curr_idx] = prefix_prod[curr_idx-1]*prev_prod
            else:
                prefix_prod[curr_idx] = prev_prod
            prev_prod *= n

        return prefix_prod


def main():
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
