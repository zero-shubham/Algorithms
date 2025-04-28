from typing import List

# https://leetcode.com/problems/longest-turbulent-subarray/submissions/1619895482/
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        mxL, mxR, l, r = 0, 0, 0, 1

        prvC = currC = "="
        while r < len(arr):

            if arr[r-1] == arr[r]:
                currC = "="
            elif arr[r-1] < arr[r]:
                currC = "<"
            elif arr[r-1] > arr[r]:
                currC = ">"

            if currC == "=":
                l = r
                prvC = currC
            elif prvC == currC:
                l = r-1
            else:
                prvC = currC

            if mxR-mxL < r-l:
                mxR = r
                mxL = l

            r += 1

        return mxR+1 - mxL


def main():
    s = Solution()
    print(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
    print(s.maxTurbulenceSize([4, 8, 12, 16]))
    print(s.maxTurbulenceSize([4]))
    print(s.maxTurbulenceSize([4, 4]))


if __name__ == "__main__":
    main()
