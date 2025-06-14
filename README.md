<img width="607" alt="image" src="https://github.com/user-attachments/assets/a30ab4b1-9faf-4ca7-905c-e18d659b7827" />

<img width="627" alt="image" src="https://github.com/user-attachments/assets/db5ed65d-1fd7-4e73-8f9b-bba11ef3bbc0" />

<img width="627" alt="image" src="https://github.com/user-attachments/assets/59cd9cf9-2c1c-4daa-a5ac-1fbb54e81498" />

<img width="627" alt="image" src="https://github.com/user-attachments/assets/7a6a9068-fe49-4ba0-bf0f-a65237661c22" />

<img width="627" alt="image" src="https://github.com/user-attachments/assets/2741bc59-c604-43cc-97df-03ebac63cbe5" />
(Even one node is disconnected, the whole graph is disconnected.)

<img width="611" alt="image" src="https://github.com/user-attachments/assets/0f7e7e74-30c7-49d7-ac42-01874e297b8c" />

<img width="635" alt="image" src="https://github.com/user-attachments/assets/2f4095e4-a3ea-4b53-a6c2-d2d1bfae0622" />

      from collections import deque

      def bfs(root):
          queue = deque([root])
          visited = set([root])
          while len(queue) > 0:
              node = queue.popleft()
              for neighbor in get_neighbors(node):
                  if neighbor in visited:
                      continue
                  queue.append(neighbor)
                  visited.add(neighbor)
<img width="634" alt="image" src="https://github.com/user-attachments/assets/9c72e9a0-9e4e-4eec-a793-2434587d5384" />

      from collections import deque

      def bfs(root):
          queue = deque([root])
          visited = set([root])
          level = 0
          while len(queue) > 0:
              n = len(queue) # get # of nodes in the current level
              for _ in range(n): # here is to track the level during traversal in bfs. 
                  node = queue.popleft()
                  for neighbor in get_neighbors(node):
                      if neighbor in visited:
                          continue
                      queue.append(neighbor)
                      visited.add(neighbor)
              # increment level after we have processed all nodes of the level
              level += 1
              
### Example of Exploring Shortest Path between two nodes using BFS:
<img width="559" alt="image" src="https://github.com/user-attachments/assets/e60d3bc9-7cd8-4cb7-8172-db22fdd86296" />

            from collections import deque
            from typing import List
            
            def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
                def get_neighbors(node: int):
                    return graph[node]
            
                # BFS template
                def bfs(root: int, target: int):
                    queue = deque([root])
                    visited = {root}
                    level = 0
                    while len(queue) > 0:
                        n = len(queue)
                        for _ in range(n): # here is to track the level during traversal in bfs. 
                            node = queue.popleft()
                            if node == target:
                                return level
                            for neighbor in get_neighbors(node):
                                if neighbor in visited:
                                    continue
                                queue.append(neighbor)
                                visited.add(neighbor)
                        level += 1
                    return level
            
                return bfs(a, b)
### Complete template for BFS on the matrix:
            num_rows, num_cols = len(grid), len(grid[0])
            def get_neighbors(coord):
                row, col = coord
                delta_row = [-1, 0, 1, 0]
                delta_col = [0, 1, 0, -1]
                res = []
                for i in range(len(delta_row)): # we do not have outer layer of for _ in range(n) here, b/c we do not need to track the level/distance. 
                    neighbor_row = row + delta_row[i]
                    neighbor_col = col + delta_col[i]
                    if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                        res.append((neighbor_row, neighbor_col))
                return res
            
            from collections import deque
            
            def bfs(starting_node):
                queue = deque([starting_node])
                visited = set([starting_node])
                while len(queue) > 0:
                    node = queue.popleft()
                    for neighbor in get_neighbors(node):
                        if neighbor in visited:
                            continue
                        # Do stuff with the node if required
                        # ...
                        queue.append(neighbor)
                        visited.add(neighbor)
<img width="635" alt="image" src="https://github.com/user-attachments/assets/d874de1c-8af1-4239-a308-6c38e15172c2" />



### Topological Sort vs BFS:
<img width="620" alt="image" src="https://github.com/user-attachments/assets/70892055-0697-4ac8-839a-07f7239855ee" />
<img width="649" alt="image" src="https://github.com/user-attachments/assets/195789ac-3091-46e6-8832-e09a679e301c" />

      from collections import deque

      def find_indegree(graph):
          indegree = { node: 0 for node in graph }  # dict
          for node in graph:
              for neighbor in graph[node]:
                  indegree[neighbor] += 1
          return indegree
      
      
      def topo_sort(graph):
          res = []
          q = deque()
          indegree = find_indegree(graph)
          for node in indegree:
              if indegree[node] == 0:
                  q.append(node)
          while len(q) > 0:
              node = q.popleft()
              res.append(node)
              for neighbor in graph[node]:
                  indegree[neighbor] -= 1
                  if indegree[neighbor] == 0:
                      q.append(neighbor)
          return res if len(graph) == len(res) else None
    
### DFS on Graph:
<img width="458" alt="image" src="https://github.com/user-attachments/assets/ade3b7bf-e1c7-4a92-9079-022d064a8e83" />
<img width="628" alt="image" src="https://github.com/user-attachments/assets/af485a91-0898-4807-b0a2-172eec2717e2" />


<img width="602" alt="image" src="https://github.com/user-attachments/assets/f0110fb9-a2f5-4fad-86e4-f444fb5cfa99" />

<img width="651" alt="image" src="https://github.com/user-attachments/assets/b7f5c85a-0727-4014-9b34-9beba407e2c3" />

### BFS vs DFS?
<img width="682" alt="image" src="https://github.com/user-attachments/assets/979514d5-843a-453b-b6e5-70dcf3e45cd8" />

### Minimum Spanning Tree!

Definition: 
A Minimum Spanning Tree is a tree with overall minimum weight generated from a graph that includes every node in the original graph. You will recall that a tree is defined as a graph with n - 1 edges, n nodes, as well as no cycles throughout the tree. We can essentially think of it as generating the tree with smallest total weight by selecting edges from a graph.

![image](https://github.com/user-attachments/assets/420e58b1-472c-4adf-8d17-c902abef315d)

![image](https://github.com/user-attachments/assets/6d0d8749-62f1-456a-bd48-61cc2a9f897c)

      class Edge:
          def __init__(self, weight, a, b):
              self.weight = weight
              self.a = a
              self.b = b
      def cmp():
          def compare(x, y):
              return x.weight < y.weight
          return compare
      def minimum_spanning_tree(n : int, edges : List[edge]) -> int:
          # sort list, make sure to define custom comparator class cmp to sort edge based on weight from lowest to highest
          edges.sort(key = cmp)
          dsu = UnionFind()
          ret, cnt = 0, 0
          for edge in edges:
            # check if edges belong to same set before merging and adding edge to mst
            if dsu.find(edge.a) != dsu.find(edge.b):
              dsu.union(edge.a, edge.b)
              ret = ret + edge.weight
              cnt += 1
              if cnt == n - 1:
                break
          return ret
          
![image](https://github.com/user-attachments/assets/b11b8f12-f115-47c7-90b3-8d71551418ab)
