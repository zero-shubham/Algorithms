from typing import List
from collections import deque

# https://leetcode.com/problems/rotting-oranges/submissions/1601426203/
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.visited = set()

        self.ROWS = len(grid)
        if self.ROWS < 1:
            return 0
        self.COLS = len(grid[0])

        t = 0
        rotten = deque()
        fresh = 0
        for row in range(0, self.ROWS):
            for col in range(0, self.COLS):
                if (row, col) not in self.visited and grid[row][col] == 2:
                    rotten.appendleft((row, col))
                if (row, col) not in self.visited and grid[row][col] == 1:
                    fresh += 1

        while rotten and fresh > 0:
            length_q = len(rotten)
            for i in range(length_q):
                r, c = rotten.popleft()
                if (r, c) in self.visited:
                    continue
                self.visited.add((r, c))
                neighbours = self.get_neighbours(grid, r, c)

                for n in neighbours:
                    if n not in rotten:
                        rotten.append(n)
                        fresh -= 1

            t += 1

        if fresh>0:
            # print(unvisited, "||", self.visited, l)
            return -1
        return t

    def get_neighbours(self, grid: List[List[int]], row: int, col: int) -> List[int]:
        neighbours = set()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if min(row+dr, col+dc) < 0 or row+dr > self.ROWS-1 or col+dc > self.COLS-1 or (row+dr, col+dc) in self.visited:
                continue

            if grid[row+dr][col+dc] == 1:
                neighbours.add((row+dr, col+dc))

        return neighbours


def main():
    s = Solution()
    print(s.orangesRotting([[2, 1, 1],
                            [0, 1, 1],
                            [1, 0, 1]]))
    print(s.orangesRotting([[2, 1, 1],
                            [1, 1, 0],
                            [0, 1, 1]]))

    print(s.orangesRotting([[2, 1, 1],
                            [1, 1, 1],
                            [0, 1, 2]]))


if __name__ == "__main__":
    main()
