from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = len(ratings)
        allocation = [1] * total

        for i in range(1, len(ratings)):
            print(allocation, total)
            if ratings[i] > ratings[i - 1] and allocation[i] <= allocation[i - 1]:
                allocation[i] = allocation[i-1] + 1
                total += 1
            if ratings[i - 1] > ratings[i] and allocation[i - 1] <= allocation[i]:
                allocation[i - 1] = allocation[i] + 1
                total += 1
        print(allocation, total, sum(allocation))
        return total


Solution().candy([1, 2, 87, 87, 87, 2, 1])
