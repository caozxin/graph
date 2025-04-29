from  collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # if not rooms:
        #     return

        num_rows, num_cols = len(rooms), len(rooms[0]) # please note num_rows != num_cols here.
        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    #if not wall:
                    if rooms[neighbor_row][neighbor_col] != -1:
                        res.append((neighbor_row, neighbor_col))
            # print(res)
            return res

        # get_neighbors((1,2)) 
        def bfs(starting_node) :
            queue = deque([starting_node])
            visited =  set([starting_node])                
            level_count = 0
            min_count = rooms[starting_node[0]][starting_node[1]]  #2147483647
            while len(queue) > 0:
                
                for _ in range(len(queue)):
                    node = queue.popleft()
                    node_val = rooms[node[0]][node[1]]
                    # print('node', node, node_val)
                    # exit()
                    # if node_val != -1 and node_val != 0:
                    if node_val == 0: # whne we found the gate, we update min_count
                        # print("found gate!", node, level_count)
                        if min_count > level_count:
                            min_count = level_count
                        # return 

                    for neighbor in get_neighbors(node):
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)
                level_count += 1

                # return level_count # if not found gate, we do not have to do anything.
                # return
            if min_count < 250: # if there is a min_count, we update it with empty space. 
                rooms[starting_node[0]][starting_node[1]] = min_count

        # bfs((0,0))
        for i in range(num_rows):
            for j in range(num_cols):
                if rooms[i][j] != 0 and rooms[i][j] != -1:
                    bfs((i,j))


### best version using bfs template:
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return

        num_rows, num_cols = len(rooms), len(rooms[0])

        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(4):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    if rooms[neighbor_row][neighbor_col] == 2147483647: # if the neighbor is empty space.
                        res.append((neighbor_row, neighbor_col))
            return res

        def bfs(queue):
            #noticed there is no visited() here. 
            while queue:
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    rooms[neighbor[0]][neighbor[1]] = rooms[node[0]][node[1]] + 1 #Each step into the dungeon will add one more level to the BFS tree. The idea here is the distance from the nearest gate to an empty space must be the shortest path. This way each empty space is only in the queue once.
                    queue.append(neighbor)

        # Instead of BFS from each empty room, BFS from all gates --> multiple sourced BFS. 
        queue = deque()
        for i in range(num_rows):
            for j in range(num_cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        bfs(queue)
