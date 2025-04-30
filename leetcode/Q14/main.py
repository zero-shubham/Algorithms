
# https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1621728764/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lptr = rptr = 0

        self.char_occur = [0]*26
        wrd_cnt = 0
        self.char_occur[ord(s[rptr])-65] += 1
        
        while rptr < len(s):
            if (rptr+1-lptr) - max(self.char_occur) <= k:
                wrd_cnt = max(rptr+1-lptr, wrd_cnt)
                # print("occurence: ", self.char_occur, lptr, rptr)
            else:
                self.char_occur[ord(s[lptr])-65] -= 1
                # print("deducted: ", self.char_occur)
                lptr += 1

            rptr += 1
            if rptr < len(s):
                self.char_occur[ord(s[rptr])-65] += 1

        return wrd_cnt


def main():
    s = Solution()
    print(s.characterReplacement("ABAB", 2))

    print(s.characterReplacement("AABABBA", 1))


if __name__ == "__main__":
    main()
