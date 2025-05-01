from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                print("leftMax: ", leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
      
      
def main():
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([4, 2, 0, 3, 2, 5]))
    print(s.trap([1]))
    print(s.trap([4, 2, 3]))
    print(s.trap([5, 4, 1, 2]))
    print(s.trap([5, 4, 3, 2, 1]))
    
    print(s.trap([5, 6, 3, 2, 1]))


if __name__ == "__main__":
    main()
