from typing import List, Dict
from collections import deque

# https://leetcode.com/problems/course-schedule/submissions/1602493448/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        depDeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            depDeg[a] += 1

        q = deque()
        for idx, deg in enumerate(depDeg):
            # print(idx, deg)
            if deg == 0:
                q.append(idx)

        while q:
            v = q.popleft()

            for neighbour in graph[v]:

                depDeg[neighbour] -= 1

                if depDeg[neighbour] == 0:
                    q.append(neighbour)

            # print(cyclDeg, v)

        return True if sum(depDeg) == 0 else False


def main():
    s = Solution()
    print(s.canFinish(2, [[1, 0], [0, 1]]))

    print(s.canFinish(3, [[2, 1], [1, 0]]))

    print(s.canFinish(3, [[1, 0], [2, 0], [0, 2]]))

    print(s.canFinish(3, [[1, 0], [0, 2], [2, 1]]))

    print(s.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))


if __name__ == "__main__":
    main()
