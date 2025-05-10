from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def find_indegree(graph):
            indegree = {node: 0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree

        def topo_sort(graph):
            res = []
            queue = deque()
            indegree = find_indegree(graph)

            for node in indegree:
                if indegree[node] == 0:
                    queue.append(node)

            while len(queue) > 0:
                node = queue.popleft()
                res.append(node)

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            if len(res) > numCourses:
                return False
            else:
                return True

        graph = {i: [] for i in range(numCourses)}
        # print(graph)
        # exit()
        for each_course in prerequisites:
            new_seq = each_course[::-1]
            # print(each_course, new_seq)
            for i in range(len(new_seq) - 1):
                if new_seq[i+1] not in graph[new_seq[i]]:
                    graph[new_seq[i]].append(new_seq[i+1])
            for num in new_seq:
                if num not in new_seq:
                    graph[num] = []

        # print(graph)
        return topo_sort(graph)
