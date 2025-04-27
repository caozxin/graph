from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        if not x and not y:
            return 0

        def knight_moves(coord):
            row, col = coord
            delta_row = [-2, -2, -1, -1, 1, 1, 2, 2]
            delta_col = [-1, 1, -2, 2, -2, 2, -1, 1]
            res = []
            for i in range(len(delta_row)):
                move_row = row + delta_row[i]
                move_col = col + delta_col[i]
                res.append((move_row, move_col))

            return res

        def bfs(starting_node):
            queue = deque([starting_node])
            visited = set([starting_node])
            steps = 0
            while len(queue) > 0:
                
                for _ in range(len(queue)):
                    node = queue.popleft()
                    # print("node", node)
                    if node == (x, y):
                        return steps
                    for each_move in knight_moves(node):
                        if each_move in visited:
                            continue

                        queue.append(each_move)
                        visited.add(each_move)

                steps += 1 # steps here is similar to level.

        return bfs((0,0))
