from typing import List, Set, Tuple

# https://leetcode.com/problems/max-area-of-island/submissions/1599629026/

class Solution:
    def __init__(self):
        self.visited = set()

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                # print(row, col)
                if grid[row][col] == 1 and (row, col) not in self.visited:
                    # print("expanding from: ", row, col)
                    area = self.expand(row, col, grid)
                    if area > max_area:
                        max_area = area

        return max_area

    def expand(self, row: int, col: int, grid: List[List[int]]) -> int:
        if min(row, col) < 0 or (row >= len(grid) or col >= len(grid[0])) or grid[row][col] == 0 or (row, col) in self.visited:
            return 0

        self.visited.add((row, col))
        # print("visited: ", (row, col))
        count = 1

        count += self.expand(row-1, col, grid)
        count += self.expand(row+1, col, grid)
        count += self.expand(row, col-1, grid)
        count += self.expand(row, col+1, grid)

        return count


def main():
    s = Solution()
    area = s.maxAreaOfIsland([
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])

    print(area)


if __name__ == "__main__":
    main()
