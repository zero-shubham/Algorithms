from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = [0]*(len(nums)+1)

        count = 0

        for idx, n in enumerate(nums):
            s = prefix_sum[idx]+n
            if s == k:
                count += 1

            prefix_sum[idx+1] = s
        print(prefix_sum)
        nums.reverse()
        for idx, n in enumerate(nums):
            s = prefix_sum[idx]+n
            if s == k:
                count += 1

            prefix_sum[idx+1] = s
        print(prefix_sum)
        return count


def main():
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))

    print(s.subarraySum([1, 2, 3], 3))

    print(s.subarraySum([1, 2, 1, 2, 1], 3))


if __name__ == "__main__":
    main()
