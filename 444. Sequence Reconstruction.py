### my not working version:

from collections import deque

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        # find_indegree of all nodes
        def find_indegree(graph):
            indegree = {node: 0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree

        # topo_sort --> TODO
        def topo_sort(graph) -> List[List[int]]:
            res = []
            queue = deque()
            indegree = find_indegree(graph)
            print("indegree", indegree)
            print("graph", graph)
            for node in indegree:
                queue.append(node)

            while len(queue) > 0:
                node = queue.popleft()
                print()
                res.append(node)
                #validation:
                # print(node, len(graph[node]), indegree[node])

                if len(graph[node])<= 0 and indegree[node] == 0:
                    return False

                print('graph[node]', graph[node])
                for neighbor in graph[node]:
                    indegree[node] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
                print('res', res)
            # return res if len(graph) == len(res) else None

        # contruct the graph: for each_num in nums, it should be dict[each_num] = [list of its outgoing edges]
        graph: dict[str, list[str]] = {t: [] for t in nums}
        # print(graph)
        for each in sequences:
            for i in range(len(each)):
                graph[each[i]] =  graph[each[i]]  + each[i+1:]
                
        # print(graph, find_indegree(graph))
        return topo_sort(graph)

# improved working version:
from collections import deque
from typing import List
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        # find_indegree of all nodes
        def find_indegree(graph):
            indegree = {node: 0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree

        # topo_sort --> TODO
        def topo_sort(graph) -> List[int]:
            res = []
            queue = deque()
            indegree = find_indegree(graph)

            for node in indegree:
                if indegree[node] == 0:
                    queue.append(node)

            while len(queue) > 0:
                if len(queue) > 1:
                    return False

                node = queue.popleft()
                res.append(node)

                # print('graph[node]', graph[node])
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            return res == nums

        # contruct the graph: for each_num in nums, it should be dict[each_num] = [list of its outgoing edges]
        # graph: dict[str, list[str]] = {t: [] for t in nums}
        # # print(graph)
        # for each in sequences:
        #     for i in range(len(each)):
        #         graph[each[i]] =  graph[each[i]]  + each[i+1:]
                
                # construct the graph
        graph = {num: [] for num in nums}
        for seq in sequences:
            for i in range(len(seq) - 1):
                if seq[i+1] not in graph[seq[i]]:
                    graph[seq[i]].append(seq[i+1])
            for num in seq:
                if num not in graph:
                    graph[num] = []

        return topo_sort(graph)

        

