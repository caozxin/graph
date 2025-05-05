### my not working version:

from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if not board:
            return -1

        goal_board = [[1,2,3],[4,5,0]] # this is given

        num_rows, num_cols = len(board), len(board[0])
        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    # if board[neighbor_row][neighbor_col] == 0: # it needs to be empty space. 
                    res.append((neighbor_row, neighbor_col)) 
            print(res)
            return res
        # def new_board_state(node, board_state):
        #     for 
        def bfs(starting_node):
            queue = deque([(starting_node, 0, board)])
            visited = set([starting_node])

            while len(queue) > 0:

                for _ in range(len(queue)): # here just to track the level during traversal in bfs. 
                    node, level, board_state = queue.popleft()
                    print("node, level, board_state," , node, level, board_state)
                    # new_board_state = board_state
                    if board_state == goal_board:
                        return level
                    # print("node, get_neighbors(node)", node, get_neighbors(node))
                    # exit()
                    for neighbor in get_neighbors(node): # the neighbor_node is always empty. 
                        if neighbor in visited:
                            continue
                        #here we update the board_state :
                        board_state[node[0]][node[1]], board_state[neighbor[0]][neighbor[1]] = board_state[neighbor[0]][neighbor[1]], 0
                        print(board_state[node[0]][node[1]], board_state[neighbor[0]][neighbor[1]],board_state )
                        
                        
                        # board_state[node[0]][node[1]], board_state[neighbor[0]][neighbor[1]] = board_state[neighbor[0]][neighbor[1]], 0
                        # if board_state[neighbor[0]][neighbor[1]] == 0:
                        #     board_state[neighbor[0]][neighbor[1]] = board_state[node[0]][node[1]]
                        #     board_state[node[0]][node[1]] = 0
                        queue.append((neighbor, level + 1, board_state))
                        
                        visited.add(neighbor)
                    exit()

            return -1 # if no path

        # we should start with empty space
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == 0:
                    bfs((i,j))


### improved version:
from collections import deque
from typing import List
import copy

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if not board:
            return -1

        goal_board = [[1, 2, 3], [4, 5, 0]]
        num_rows, num_cols = len(board), len(board[0])

        def serialize(board):
            return tuple(tuple(row) for row in board)

        def get_neighbors(coord):
            row, col = coord
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            res = []
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    res.append((nr, nc))
            return res

        def bfs(starting_zero):
            initial_state = serialize(board)
            queue = deque([(starting_zero, 0, board)])
            visited = set([initial_state])

            while queue:
                zero_pos, level, current_board = queue.popleft()

                if current_board == goal_board:
                    return level

                for neighbor in get_neighbors(zero_pos):
                    # Swap zero with the neighbor
                    new_board = [row[:] for row in current_board]  # deep copy
                    r1, c1 = zero_pos
                    r2, c2 = neighbor
                    new_board[r1][c1], new_board[r2][c2] = new_board[r2][c2], new_board[r1][c1]

                    serialized = serialize(new_board)
                    if serialized not in visited:
                        visited.add(serialized)
                        queue.append(((r2, c2), level + 1, new_board))

            return -1

        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == 0:
                    return bfs((i, j))

        return -1
