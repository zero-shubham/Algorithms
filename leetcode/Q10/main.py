class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2

        self.cache = dict()
        return self.recLong(0, 0)

    def recLong(self, t1: int, t2: int) -> int:
        # print(text1, text2)
        if (t1, t2) in self.cache:
            return self.cache[(t1, t2)]
        if t1 >= len(self.text1) or t2 >= len(self.text2):
            return 0

        cnt = 0
        i, j = t1, t2

        while i <= len(self.text1)-1 and j <= len(self.text2)-1 and self.text1[i] == self.text2[j]:
            cnt += 1
            i += 1
            j += 1

        if i <= len(self.text1)-1 and j <= len(self.text2)-1:
            cnt += max(self.recLong(i, j+1),
                       self.recLong(i+1, j))
        self.cache[(t1, t2)] = cnt
        return cnt


def main():
    s = Solution()
    print(s.longestCommonSubsequence("ace", "abcde"))

    print(s.longestCommonSubsequence("psnw", "vozsh"))
    print(s.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"))
    print(s.longestCommonSubsequence("ezupkr", "ubmrapg"))


if __name__ == "__main__":
    main()
