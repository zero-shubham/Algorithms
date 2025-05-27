from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset = []
        self.backtrack(0, n, k, [], subset)
        return subset

    def backtrack(self, i: int, n: int, k: int, curset: List[int], subset: List[List[int]]):
        if len(curset) >= k:
            subset.append(curset.copy())
            return

        if i >= n:
            return

        for j in range(i+1, n+1):
            curset.append(j)
            self.backtrack(j, n, k, curset, subset)
            curset.pop()


def main():
    s = Solution()
    print(s.combine(5, 2))


if __name__ == "__main__":
    main()
