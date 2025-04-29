from typing import List

# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/1620776707/
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k-1])
        cnt = 0
        for idx, rPtr in enumerate(arr[k-1:]):
            s += rPtr
            if s/k >= threshold:
                cnt += 1

            s -= arr[idx]

        return cnt


def main():
    s = Solution()
    print(s.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))


if __name__ == "__main__":
    main()
