from typing import List

# inefficient n^2 time

# https://leetcode.com/problems/trapping-rain-water/submissions/1622679474/
class Solution:
    def trap(self, height: List[int]) -> int:
        i = j = 0
        res = 0

        while i < len(height):
            rMaxIdx = j
            # find the next wall that can trap max water with current wall
            while j < len(height):
                if height[j] >= height[rMaxIdx]:
                    rMaxIdx = j
                if height[j] >= height[i]:
                    break
                j += 1

            # print(i, rMaxIdx, j)
            k = i+1

            # add up the water between walls
            while k <= rMaxIdx and k < len(height):
                # print(i, nm, k, min(height[i], height[nm]))
                res += max(min(height[i], height[rMaxIdx])-height[k], 0)
                k += 1

            i = rMaxIdx
            j = i+1

        return res


def main():
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([4, 2, 0, 3, 2, 5]))
    print(s.trap([1]))
    print(s.trap([4, 2, 3]))
    print(s.trap([5, 4, 1, 2]))
    print(s.trap([5, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
