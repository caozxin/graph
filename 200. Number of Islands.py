### my version with bfs:

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows , num_cols = len(grid), len(grid[0])
        num_islands = 0
        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
            

                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    # print(grid[neighbor_row][neighbor_col], type(grid[neighbor_row][neighbor_col]))
                    if grid[neighbor_row][neighbor_col] == "1":
                        # print("neighbor", neighbor_row, neighbor_col, grid[neighbor_row][neighbor_col])
                        res.append((neighbor_row, neighbor_col))

            return res

        # print(get_neighbors((3,3)))
        # return 0
        def bfs(starting_node):
            queue = deque([starting_node])
            visited = set([starting_node])
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    # print("neighbor", neighbor)
                    if neighbor in visited:
                        continue

                    queue.append(neighbor)
                    visited.add(neighbor)
                    grid[neighbor[0]][neighbor[1]] = "checked"
            # print("visited", visited)
            # print(grid)
            

        # bfs((0,0))
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1":
                    bfs((i,j))
                    num_islands += 1
                else:
                    continue
        # print("num_islands", num_islands)
        return num_islands

### best version with iterative dfs:
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    stack = [(r, c)]
                    grid[r][c] = "0"  # mark as visited immediately

                    while stack:
                        x, y = stack.pop()
                        if x > 0 and grid[x-1][y] == "1":
                            stack.append((x-1, y))
                            grid[x-1][y] = "0"
                        if x < rows-1 and grid[x+1][y] == "1":
                            stack.append((x+1, y))
                            grid[x+1][y] = "0"
                        if y > 0 and grid[x][y-1] == "1":
                            stack.append((x, y-1))
                            grid[x][y-1] = "0"
                        if y < cols-1 and grid[x][y+1] == "1":
                            stack.append((x, y+1))
                            grid[x][y+1] = "0"

        return num_islands

