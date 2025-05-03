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
                    if board[neighbor_row][neighbor_col] == 0: # it needs to be empty space. 
                        res.append((neighbor_row, neighbor_col)) 
            print(res)
            return res
        
        def bfs(starting_node, target):
            queue = deque([(starting_node, 1, board_state)])
            visited = set([starting_node])

            while len(queue) > 0:

                for _ in range(len(queue)): # here just to track the level during traversal in bfs. 
                    node, level, board_state = queue.popleft()
                    new_board_state = board_state
                    if new_board_state == goal_board:
                        return level

                    for neighbor in get_neighbors(node):
                        
