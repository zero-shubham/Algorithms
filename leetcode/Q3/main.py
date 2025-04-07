from typing import List



def jump(nums: List[int]) -> int:
    step = 0
    lp = rp = 0
    while rp <= len(nums)-1:
        max_range = 0
        for i in range(lp, rp+1):
            max_range = max(max_range, i+nums[i])
        lp = rp+1
        rp = max_range
        step += 1
    return step


def main():
    # print(jump([2, 1]))
    # print(jump([1, 2]))
    print(jump([2, 3, 1, 1, 4, 5]))
    # print(jump([1, 2, 3]))
    print(jump([2, 3, 1, 1, 4]))

    # print(jump([1, 2, 1, 1, 1]))

    # print("=======")
    # print(jump([1, 3, 2]))


if __name__ == "__main__":
    main()
