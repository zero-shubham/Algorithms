from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == word[0]:

                    if self.expand(row, col, board, word, set(), 0):
                        return True

        return False

    def expand(self, row: int, col: int, board: List[List[str]], word: str, visited: Set, ptr: int) -> bool:
        if min(row, col) < 0 or (row >= len(board) or col >= len(board[0])) or board[row][col] != word[ptr]:
            return False

        if (row, col) in visited:
            return False

        visited.add((row, col))

        if ptr == (len(word)-1):
            return True

        ptr += 1

        if self.expand(row-1, col, board, word, visited, ptr):
            return True

        if self.expand(row+1, col, board, word, visited, ptr):
            return True

        if self.expand(row, col-1, board, word, visited, ptr):
            return True

        if self.expand(row, col+1, board, word, visited, ptr):
            return True

        visited.remove((row, col))
        return False


def main():
    s = Solution()
    print(s.exist([["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]],
                  "SEE"))
    print(s.exist([["A", "B", "C", "E"],
                   ["S", "F", "C", "S"],
                   ["A", "D", "E", "E"]],
                  "ABCB"))
    print(s.exist([["C", "A", "A"],
                   ["A", "A", "A"],
                   ["B", "C", "D"]],
                  "AAB"))
    print(s.exist([["A", "B", "C", "E"],
                   ["S", "F", "E", "S"],
                   ["A", "D", "E", "E"]],
                  "ABCESEEEFS"))


if __name__ == "__main__":
    main()
