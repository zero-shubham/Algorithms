from typing import List

map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1645686023/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combo = []
        self.backtrack(0, digits, [], combo)
        return combo

    def backtrack(self, i: int, digits: str, curset: list, combo: list):
        if len(digits) < 1:
            return

        if len(curset) >= len(digits):
            combo.append("".join(curset))

        if i >= len(digits):
            return
        for j in map[digits[i]]:
            curset.append(j)
            self.backtrack(i+1, digits, curset, combo)
            curset.pop()


def main():
    s = Solution()
    print(s.letterCombinations("23"))


if __name__ == "__main__":
    main()
