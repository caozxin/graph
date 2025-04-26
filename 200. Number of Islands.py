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
            print("visited", visited)
            print(grid)
            

        # bfs((0,0))
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1":
                    bfs((i,j))
                    num_islands += 1
                else:
                    continue
        print("num_islands", num_islands)
        return num_islands
