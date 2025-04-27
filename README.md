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
              for _ in range(n):
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
                        for _ in range(n):
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
                for i in range(len(delta_row)):
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

<img width="458" alt="image" src="https://github.com/user-attachments/assets/ade3b7bf-e1c7-4a92-9079-022d064a8e83" />

<img width="628" alt="image" src="https://github.com/user-attachments/assets/af485a91-0898-4807-b0a2-172eec2717e2" />

<img width="602" alt="image" src="https://github.com/user-attachments/assets/f0110fb9-a2f5-4fad-86e4-f444fb5cfa99" />

<img width="651" alt="image" src="https://github.com/user-attachments/assets/b7f5c85a-0727-4014-9b34-9beba407e2c3" />

### BFS vs DFS?
<img width="682" alt="image" src="https://github.com/user-attachments/assets/979514d5-843a-453b-b6e5-70dcf3e45cd8" />

