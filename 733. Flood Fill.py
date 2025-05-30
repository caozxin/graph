from collections import deque # we need it to use BFS. 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #none handling:
        if not image:
            return [] # this should be matching return format. 
        targeted_color = image[sr][sc]
        # print(targeted_color, type(targeted_color))
        num_rows, num_cols = len(image), len(image[0]) # please note matrix is always square.
        # print(num_rows, num_cols)

        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0] # row only moves up and down. 
            delta_col = [0, 1, 0, -1] # col only moves left and right
            res = []
            for i in range(len(delta_row)): # len(delta_row) == len(delta_col) = 4 directions.
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row <num_rows and 0 <= neighbor_col < num_cols: # validate both neighbor_row and neighbor_col. 
                    res.append((neighbor_row, neighbor_col)) # matching List[List[int]]. 
            return res

        def bfs(starting_node):
            queue = deque([starting_node])
            visited = set([starting_node])

            while len(queue) > 0:
                node = queue.popleft()
                i,j = node[0], node[1]
                if image[i][j] == targeted_color:
                    image[i][j] = color

                    for neighbor in get_neighbors(node):
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)

        # print(get_neighbors((sr,sc)))
        bfs((sr,sc))
        return image
