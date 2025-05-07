from collections import deque

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:

        # find_indegree of all nodes
        
        # topo_sort

        # contruct the graph: for each_num in nums, it should be dict[each_num] = [list of its outgoing edges]
        graph: dict[str, list[str]] = {t: [] for t in nums}
        # print(graph)
        for each in sequences:
            for i in range(len(each)):
                print(each[i], each[i+1:])
                graph[each[i]] =  graph[each[i]]  + each[i+1:]
                
        print(graph)
