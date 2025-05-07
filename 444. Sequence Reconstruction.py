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
            print(indegree)
            for node in indegree:
                queue.append(node)

            while len(queue) > 0:
                node = queue.popleft()
                res.append(node)
                for neighbor in graph[node]:
                    indegree[node] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            print(res)
            # return res if len(graph) == len(res) else None

        # contruct the graph: for each_num in nums, it should be dict[each_num] = [list of its outgoing edges]
        graph: dict[str, list[str]] = {t: [] for t in nums}
        # print(graph)
        for each in sequences:
            for i in range(len(each)):
                graph[each[i]] =  graph[each[i]]  + each[i+1:]
                
        # print(graph, find_indegree(graph))
        topo_sort(graph)

        
