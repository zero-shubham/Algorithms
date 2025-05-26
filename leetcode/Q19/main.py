from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = []  # Max heap
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        min_capital.sort()

        for _ in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = min_capital.pop(0)
                heapq.heappush(max_profit, -p)

            if not max_profit:
                break

            w += -heapq.heappop(max_profit)

        return w


def main():
    s = Solution()

    print(
        s.findMaximizedCapital(
            k=2,
            w=0,
            profits=[1, 2, 3],
            capital=[0, 1, 1])
    )

    print(
        s.findMaximizedCapital(
            k=1,
            w=2,
            profits=[1, 2, 3],
            capital=[1, 1, 2])
    )

    print(
        s.findMaximizedCapital(
            k=3,
            w=0,
            profits=[1, 4, 2, 3],
            capital=[0, 3, 1, 1])
    )


if __name__ == "__main__":
    main()
