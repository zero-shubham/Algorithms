from typing import List, Dict

# https://leetcode.com/problems/course-schedule/submissions/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        # construct graph
        for a, b in prerequisites:
            graph[b].append(a)

        visiting = set()
        for vertex, edges in graph.items():

            if not self.dfs_is_not_cyclic(graph, visiting, vertex):
                return False

        return True

    def dfs_is_not_cyclic(self, graph: Dict[int, List[int]], visiting: set, vertex: int) -> bool:
        if vertex in visiting:
            # print(vertex, visiting)
            return False

        if len(graph[vertex]) < 1:
            return True
        is_not_cyclic = True
        visiting.add(vertex)
        for n in graph[vertex]:
            # print("neighbours: ", graph[vertex])
            # print("visiting: ", visiting)
            is_not_cyclic = is_not_cyclic and self.dfs_is_not_cyclic(
                graph, visiting, n)
        visiting.remove(vertex)
        graph[vertex] = []  # mark sub graph from this vertex has no cycles

        return is_not_cyclic


def main():
    s = Solution()
    print(s.canFinish(2, [[1, 0], [0, 1]]))

    print(s.canFinish(3, [[2, 1], [1, 0]]))

    print(s.canFinish(3, [[1, 0], [2, 0], [0, 2]]))

    print(s.canFinish(3, [[1, 0], [0, 2], [2, 1]]))

    print(s.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))


if __name__ == "__main__":
    main()
